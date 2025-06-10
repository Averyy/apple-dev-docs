# Creating drivers for iPadOS

**Framework**: DriverKit

Bring your drivers to iPadOS by using the platform’s DriverKit support.

#### Overview

In iPadOS 16 and later, you can develop drivers that run on macOS and iPadOS using DriverKit. The DriverKit frameworks provide a safe and secure approach to creating drivers for external USB and Thunderbolt devices that people can connect to their iPad.

iPadOS 16 supports the core [`DriverKit`](DriverKit.md) framework, as well as the following:

- [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit)
- [`PCIDriverKit`](https://developer.apple.com/documentation/PCIDriverKit)
- [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit)

> **Note**:  DriverKit on iPadOS requires an iPad with an M-series chip.

##### Add a Driverkit Target to Your Xcode Project

If you’re creating a new app in Xcode, use the Multiplatform App template when you create your project in Xcode. The app you create is what people use to install and update your driver on their macOS and iPadOS devices. To add a driver to your project, add a new target to your project by choosing DriverKit from the tab bar, and select the Driver target.

![The template selection dialog for a new target in Xcode. The tab bar shows DriverKit selected, and the selected template is the Driver target template.](https://docs-assets.developer.apple.com/published/b7d598aa95dc2cf2247bfbd01692c16e/media-4037570%402x.png)

If you already have a DriverKit project for macOS, you can support iPadOS by editing your project settings. Select the project from the Navigator, select the app target, and choose General from the tab bar. In the Supported Destinations section, use the Add (+) button to add a new iPad destination.

![The Supported Destinations section of an app target’s General tab. The list shows two destinations: iPad (whose associated SDK is iOS) and Mac (whose associated SDK is macOS).](https://docs-assets.developer.apple.com/published/948573b8caf99f17a3158303a1ab4965/media-4034747%402x.png)

##### Install a Driver

On macOS, your host app uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install a driver onto the host system. On iPadOS, this framework is absent, so this step is unneccessary. If you’re writing a driver to run on both platforms, conditionalize your app code so you only call [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) on macOS.

```swift
#if os(macOS)
    // Call SystemExtensions framework to install your driver.
#endif
```

Because drivers operate with enhanced privileges, a person using the device needs to approve any driver before it can run. On macOS, they grant this permission in System Settings > Privacy & Security.

On iPadOS, there are two locations in the Settings app for managing drivers:

- If the iPad has at least one driver installed, Settings > General > Drivers lists all available drivers on the device. A person using the iPad can toggle each driver on or off individually.
- If your app contains a Settings bundle, Settings > Your-App-Name > Drivers lists the drivers installed by your app, with toggles to enable them. Your app needs to prompt the person to enable the driver in the Settings app.

After receiving permission, the driver runs on-demand. For example, a driver for an audio interface only runs when someone connects that hardware to their device.

##### Allow User Clients to Attach to Your Driver

Some apps need to communicate with a running driver. The sample code project, [`Communicating between a DriverKit extension and a client app`](communicating-between-a-driverkit-extension-and-a-client-app.md), provides an example of how to do this.

To allow user clients to connect to your driver, you need specific entitlements, based on the nature of your driver.

- On macOS, use the [`com.apple.developer.driverkit.userclient-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access) entitlement. Provide an array of allowed bundle identifiers as the value of this entitlement. Only apps with these bundle identifiers can connect to the driver at runtime.
- On iPadOS, use the [`Communicates with Drivers`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.communicates-with-drivers) entitlement. This entitlement takes a Boolean value; set it to `YES` to allow your user client to connect to drivers.
- If your iPadOS driver works with many apps, use the [`DriverKit Allow Third Party User Clients`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.allow-third-party-userclients) entitlement. Set the Boolean value of this entitlement to `YES` to allow any app to connect to your driver.

## See Also

- [Implementing drivers, system extensions, and kexts](../kernel/implementing_drivers_system_extensions_and_kexts.md)
  Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/creating-drivers-for-ipados)*