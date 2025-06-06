# Requesting Entitlements for DriverKit Development

**Framework**: Driverkit

Request the entitlement for DriverKit development, and request other entitlements your driver needs to interact with specific devices and interfaces.

#### Overview

DriverKit services communicate with sensitive parts of the system, including kernel objects and attached hardware peripherals. To ensure that these interactions don’t compromise the security or integrity of the system, the system loads only drivers that have a valid set of entitlements. The DriverKit entitlements give your driver permission to run as a driver, define the type of hardware your driver supports, and sometimes define the family to which your driver belongs.

When you develop a DriverKit extension, you deliver that extension inside in a specific directory of your app bundle. The app handles the activation of your extension, which registers it with the system and makes its services available for use. To perform this installation, your app must have the System Extension entitlement.

##### Gather Information About Your Hardware Devices

Before you request entitlements, gather information about the hardware devices for which you’ll need drivers. Specifically, you’ll need the following information:

- The transport mechanism for your hardware. DriverKit supports USB, PCI, HID, networking, and serial devices.
- Your company’s hardware vendor ID for the type of devices.
- Brief descriptions of the devices.
- A brief description of the app you’ll use to install the driver.

##### Request the Driverkit Entitlements You Need

Before you begin developing drivers for your hardware, request the entitlements you need from Apple:

1. Go to [`https://developer.apple.com/system-extensions/`](https://developer.apple.comhttps://developer.apple.com/system-extensions/) and click the link to request an entitlement.
2. Apply for the DriverKit entitlement and specify the entitlements you need.
3. Provide a description of the apps you’ll use to support your hardware.

Apple ties any requested entitlements to your development team’s profile. When making the request, specify the complete set of entitlements you use to support one product. For example, when developing HID devices, you might ask Apple to create a single group that contains the [`com.apple.developer.driverkit`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit), [`com.apple.developer.driverkit.transport.hid`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.hid), and [`com.apple.developer.driverkit.family.hid.eventservice`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice) entitlements. All of the requested entitlements must belong to the same group.

> **Note**:  While waiting for Apple to grant your entitlement requests, you can continue to develop and test your drivers on your local systems. For information about how to disable the necessary security checks, see [`Debugging and testing system extensions`](debugging-and-testing-system-extensions.md).

##### Update Your Drivers Entitlements File

Xcode provides a default entitlements file for every new DriverKit driver you create. This file is separate from your app’s entitlements file, and contains only the entitlements that your driver needs to run.

Edit your driver’s entitlements file and add the entitlements that match the services your driver offers. The default driver entitlements file contains only the DriverKit and App Sandbox entitlements. Most drivers require a transport-specific entitlement to tell the system what type of hardware they support. For example, a driver that implements an event service to communicate with a HID device must include the following entitlements in its entitlements file:

- [`com.apple.developer.driverkit.transport.hid`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.hid)
- [`com.apple.developer.driverkit.family.hid.eventservice`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice)

When activating your driver, the system validates the entitlements in your driver’s entitlements file with the information you used to codesign your driver. If the entitlements don’t match, the system aborts the activation process.

For infomation about specific entitlements, see the reference documentation.

##### Configure Your Drivers Provisioning Profile

To distribute a driver using the entitlements that Apple provides, go to the Certificates, Identifiers & Profiles section of the Apple developer portal ([`https://developer.apple.com`](https://developer.apple.comhttps://developer.apple.com)) and do the following:

- [`Configure an App ID`](https://developer.apple.comhttps://help.apple.com/developer-account/#/dev1b35d6f83) for your driver, in the Identifiers section.
- [`Configure a provisioning profile`](https://developer.apple.comhttps://help.apple.com/developer-account/#/devbd904d1a5) for your App ID, in the Profiles section.

When you create the provisioning profile for your driver, the portal prompts you to select any additional entitlements to include with your profile. Select the DriverKit-related entitlements group that Apple added to your development team. You can select only one group, so that group must contain all of the entitlements your driver needs to operate. Download the resulting provisioning profile and configure it as the provisioning profile for your driver.

> **Note**:  During development, you can temporarily disable the normal security checks to simplify the debugging process for your drivers. For more information, see [`Debugging and testing system extensions`](debugging-and-testing-system-extensions.md).

##### Add the System Extension Capability to Your App

The app you use to deliver your driver to users must also have specific entitlements to support the activation process. To add these entitlements to your app, enable the System Extension capability for your app target.

1. Open your app project in Xcode.
2. Select your app target.
3. Navigate to the Signing & Capabilities tab.
4. [`Add the System Extension capability`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev88ff319e7).

For more information about how to install drivers, see `Installing System Extensions and Drivers`.

## See Also

- [com.apple.developer.driverkit](../BundleResources/Entitlements/com.apple.developer.driverkit.md)
  A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](../BundleResources/Entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](../BundleResources/Entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DriverKit/requesting-entitlements-for-driverkit-development)*