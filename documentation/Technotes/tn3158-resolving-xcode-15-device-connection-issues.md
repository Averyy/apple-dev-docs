# TN3158: Resolving Xcode 15 device connection issues

**Framework**: Technotes

Identify software preventing Xcode 15 from connecting to Apple devices, and modify your configuration to allow these connections.

#### Overview

Xcode 15 uses a network-based interface to communicate with Apple devices connected to the Mac with a USB cable. In some environments, network management software may interfere with Xcode’s ability to connect to these devices. These configurations include:

- VPN apps using Packet Filter (PF) rules
- VPN apps using a Network Extension provider with [`includeAllNetworks`](https://developer.apple.com/documentation/NetworkExtension/NEVPNProtocol/includeAllNetworks) enabled
- Security configurations using PF

These configurations can prevent the link-local IPv6 traffic that Xcode uses to communicate with a connected Apple device from reaching the device. If you’re a VPN developer or IT professional, follow this document to verify what parts of your configuration affect Xcode, and how to modify your configuration to avoid blocking Xcode’s device communication network traffic. If you’re an app developer in a large organization experiencing device connection issues with Xcode 15, you may need to get assistance from your IT department. If you’re an app developer using a commercial VPN or security product not administered by an IT department, contact the vendor for assistance.

#### Create a Test Environment

Create an isolated test environment to confirm any device connection issues you are experiencing, and then identify the specific parts of your configuration preventing Xcode’s connection to an attached Apple device. A complex environment may have multiple pieces of software installed that affect Xcode’s ability to communicate with connected devices, such as a VPN, a security configuration, or both.

If you are a VPN developer, plan on testing your VPN product without any other software installed on the Mac other than Xcode 15. If you are an IT administrator, create a list of every configuration requirement for macOS in your organization, including VPN products and security requirements, and plan on testing each part of the configuration from the list.

To run your tests, create a fresh installation of macOS 14 on the Mac you will use for testing, and only install Xcode 15. This is so that you have a clean system with no other software installed that could affect the results of your testing. In Xcode, create a new app using one of Xcode’s templates, and select the test device connected to the Mac through USB as the build destination to prepare to run the app.

> ❗ **Important**: Before running the app for the first time, verify that Xcode’s connection to the device is through USB and not a standard network interface, such as Wi-Fi or Ethernet.

To verify the type of connection Xcode is using with the Apple device, open Window > Devices and Simulators, and locate the device in the sidebar. If the connection to the device is using a standard network interface, Xcode places a globe icon next to the device name. To have Xcode use the USB connection instead, disconnect the Mac from the network, such as by shutting off Wi-Fi or disconnecting Ethernet. Once Xcode has reconnected to the device through USB, the globe icon will disappear. Once you’ve confirmed Xcode is using a USB connection to the test device, run the test app on the device.

Once you’ve successfully run the test app for the first time on the connected device, install or enable the first item from your list of configuration requirements. Rerun the test app from Xcode to verify that Xcode can still communicate with the device. If Xcode cannot run the app after installing or enabling a specific item from your configuration requirements, that software needs an update to avoid blocking Xcode’s device communication. When you find a part of your configuration that blocks Xcode’s device communication, uninstall it, and continue to apply additional items from your list of configuration requirements to test for any other software in your configuration affecting Xcode.

After confirming the software affecting Xcode’s connection to a connected device, the way you proceed depends if you can modify the software’s configuration, or if you need to work with the vendor:

- If you’re a VPN developer or an IT professional that can modify your security configuration, proceed with this document.
- If you’ve identified a software product from a vendor as the source of the issue, contact the vendor for support.

#### Update Software Using Packet Filtering Rules

If your VPN product or security configuration uses PF to filter network packets, update your PF rules to allow traffic on the network interfaces Xcode uses for device communication. These rules need to be continuously updated, as the network interfaces Xcode uses to communicate with a connected device changes over time.

To monitor for network interface changes, use [`NWPathMonitor`](https://developer.apple.com/documentation/Network/NWPathMonitor), or create a [`nw_path_monitor_t`](https://developer.apple.com/documentation/Network/nw_path_monitor_t) through [`nw_path_monitor_create()`](https://developer.apple.com/documentation/Network/nw_path_monitor_create()). Each time the path monitor notifies you that the network interfaces changed, use `ioctl` with a `SIOCGIFDIRECTLINK` request to identify the multiple network interfaces Xcode uses for device connection traffic. The system marks these interfaces with the `ifr_is_directlink` flag. Configure your PF rules to allow any IPv6 traffic on interfaces marked with this flag through the filter.

```c
/**
 Tests whether an interface is a direct-link interface.
 - Parameter name: The BSD interface name, for example, `en0`.
 - Returns 1 if it is a direct-link interface, 0 if it’s not, and -1 if an error occurred.
    In the last case, see `errno` for the error code.
 */
int isDirectLinkInterface(const char * name) {
    int fd = socket(PF_INET, SOCK_DGRAM, 0);
    if (fd < 0) {
        return -1;
    }

    struct ifreq ifr = { 0 };
    strlcpy(ifr.ifr_name, name, sizeof(ifr.ifr_name));
    int success = ioctl(fd, SIOCGIFDIRECTLINK, &ifr) >= 0;
    if (!success) {
        int error = errno;
        (void) close(fd);
        errno = error;
        return -1;
    }
    
    (void) close(fd);
    return ifr.ifr_ifru.ifru_is_directlink != 0;
}
```

The `SIOCGIFDIRECTLINK` API was added in macOS 14.4, and requires building your software with Xcode 15.3. If you’re using an older version of macOS, you need to upgrade to macOS 14.4.

> ❗ **Important**: If you maintain a VPN product that uses PF rather than a Network Extension provider, make a plan to migrate to a Network Extension provider. See [`TN3165: Packet Filter is not API`](tn3165-packet-filter-is-not-api.md).

#### Review If Your Vpn Requires Sending All Network Traffic Over the Tunnel

VPN products based on the [`NEVPNProtocol`](https://developer.apple.com/documentation/NetworkExtension/NEVPNProtocol) interface should review their use of the `includeAllNetworks` property. If `includeAllNetworks` is required for your configuration, set [`excludeDeviceCommunication`](https://developer.apple.com/documentation/NetworkExtension/NEVPNProtocol/excludeDeviceCommunication) to `true` so that Xcode’s device communication is omitted from your tunnel.

#### Revision History

-  Updated guidance for macOS 14.4 and Xcode 15.3.
-  Created initial version.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3158-resolving-xcode-15-device-connection-issues)*