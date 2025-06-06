# TN3111: iOS Wi-Fi API overview

**Framework**: Technotes

Explore the various Wi-Fi APIs available on iOS and their expected use cases.

#### Overview

iOS does not have a general-purpose API for Wi-Fi scanning and configuration.  However, it does support a wide range of special-purpose Wi-Fi APIs.  This technote lists some use cases supported by those special-purpose APIs.

#### Navigate an Internet Hotspot

If your app helps the user navigate an internet hotspot — a Wi-Fi network where the user must interact with the network to gain access to the wider internet — adopt the [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper) API.

To use `NEHotspotHelper` you must first be granted a special entitlement (`com.apple.developer.networking.HotspotHelper`) by Apple.  For information on how to apply for this, see [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper).

> ❗ **Important**: `NEHotspotHelper` is  useful for hotspot integration. There are both technical and business restrictions that prevent it from being used for other tasks, such as accessory integration or Wi-Fi based location.

`NEHotspotHelper` is  useful for hotspot integration. There are both technical and business restrictions that prevent it from being used for other tasks, such as accessory integration or Wi-Fi based location.

#### Add an Accessory to the Users Network

If you’re creating a hardware accessory and you want to make it easy for the user to add it to their local network, your best option is to build your accessory with that in mind.  Use one of these approaches:

- Wireless Accessory Configuration (WAC) — The user can configure a WAC-capable accessory directly in Settings.  Optionally, use [`EAWiFiUnconfiguredAccessoryBrowser`](https://developer.apple.com/documentation/ExternalAccessory/EAWiFiUnconfiguredAccessoryBrowser) to integrate accessory configuration directly in your app.
- HomeKit — Call `HMHome` APIs like [`performAccessorySetup(using:completionHandler:)`](https://developer.apple.com/documentation/HomeKit/HMAccessorySetupManager/performAccessorySetup(using:completionHandler:)) to ask the system to scan for, pair, and configure any unpaired HomeKit accessories .

> ❗ **Important**: To add WAC or HomeKit support to your accessory, join the [`MFi Program`](https://developer.apple.comhttps://mfi.apple.com/).

To add WAC or HomeKit support to your accessory, join the [`MFi Program`](https://developer.apple.comhttps://mfi.apple.com/).

If your accessory does not support WAC or HomeKit, you can build an accessory configuration experience on top of `NEHotspotConfigurationManager`, although this will not be as seamless as the WAC and HomeKit accessory experience.  For an example of how you might approach this, see [`Configuring a Wi-Fi accessory to join a network`](https://developer.apple.com/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network).

#### Temporarily Join a Network

If your app needs to temporarily join a Wi-Fi network — for example, you want to interact with a Wi-Fi enabled accessory with its own independent network — use `NEHotspotConfigurationManager` and set [`joinOnce`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfiguration/joinOnce) to true.  For more details, see [`Wi-Fi configuration`](https://developer.apple.com/documentation/NetworkExtension/wi-fi-configuration).

If you’re working with a Wi-Fi accessory, use [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) to simplify discovery and configuration of your accessory.

#### Permanently Join a Network

Some apps need to configure the iOS device to permanently join a Wi-Fi network, as if the user had selected the network in Settings > Wi-Fi.  For example, an app from an ISP might do this to get the user’s iOS device on to the Wi-Fi network published by a new DSL gateway that they’ve just installed.  If your app needs to do this, use `NEHotspotConfigurationManager` and set [`joinOnce`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotConfiguration/joinOnce) to false.  For more details, see [`Wi-Fi configuration`](https://developer.apple.com/documentation/NetworkExtension/wi-fi-configuration).

#### Peer to Peer Networking

If your goal is to communicate with other nearby devices, look at:

- [`Network`](https://developer.apple.com/documentation/Network) framework
- [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity) framework

Both of these support networking over peer-to-peer Wi-Fi.  In Network framework you must opt in to this via the [`includePeerToPeer`](https://developer.apple.com/documentation/Network/NWParameters/includePeerToPeer) property.  For more information about peer-to-peer networking, see [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md).

> ❗ **Important**: The on-the-wire protocol used by these peer-to-peer networking APIs is not documented for third-party use, so this technique only works between Apple devices.

The on-the-wire protocol used by these peer-to-peer networking APIs is not documented for third-party use, so this technique only works between Apple devices.

#### Location Tracking

If you’d like to use Wi-Fi data to determine the device’s location, use Core Location.  This locates the device using a wide variety of techniques, including Wi-Fi.  For more information, see [`Maps and Location`](https://developer.apple.comhttps://developer.apple.com/maps/).

#### Current Wi Fi Network

If you need to know the name of the device’s current Wi-Fi network, call [`fetchCurrent(completionHandler:)`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotNetwork/fetchCurrent(completionHandler:)).  That method requires iOS 14 or later.  On older systems, call [`CNCopyCurrentNetworkInfo`](https://developer.apple.com/documentation/systemconfiguration/1614126-cncopycurrentnetworkinfo).

#### Revision History

-  Added information about AccessorySetupKit.  Added a link to TN3151.  Made other minor editorial changes.
-  Made minor editorial changes.
-  Republished as TN3111.  Broke the content into task-focused sections.  Added a link to [`Configuring a Wi-Fi accessory to join a network`](https://developer.apple.com/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network).  Added a reference to [`fetchCurrent(completionHandler:)`](https://developer.apple.com/documentation/NetworkExtension/NEHotspotNetwork/fetchCurrent(completionHandler:)).  Updated the text for the new publication platform.
-  Added information about `NEHotspotConfigurationManager`.
-  First published as QA1942 ”iOS Wi-Fi Management APIs”.

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
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3111-ios-wifi-api-overview)*