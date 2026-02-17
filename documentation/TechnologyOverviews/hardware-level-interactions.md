# Hardware-level interactions

**Framework**: Technology Overviews

Communicate with connected hardware and write code that runs well on Apple silicon.

Apple uses system frameworks to insulate apps from the underlying hardware, but sometimes those frameworks provide only a thin layer between your app and the hardware. Apps can communicate with wired and wireless accessories using industry-standard protocols that the accessory supports. Companies that manufacture accessories can also write custom software drivers to make proprietary features available to their own apps or the system.

Apple silicon provides developers with optimization opportunities for their software. Take advantage of Apple silicon features to improve your code’s performance and power usage.

#### Access a Connected Accessory From Your App

The [`Made for iPhone (MFi) program`](https://developer.apple.comhttps://mfi.apple.com/) helps you create accessories that incorporate Apple licensed technologies. A hardware manufacturer might use this program to add AirPlay, HomeKit, and other features to an accessory that otherwise supports industry-standard connection and communication protocols.

When someone connects an MFi accessory to their iPhone or iPad using a physical cable or wireless connection, connect to that device using the [`External Accessory`](https://developer.apple.com/documentation/ExternalAccessory) framework. This framework manages the connection to the device, and you choose one of the communication protocols the device supports. Most devices support both industry-standard and manufacturer-specific protocols. For example, a wireless blood pressure cuff might support sending blood pressure data to your app. Choose the appropriate protocol and configure a [`EASession`](https://developer.apple.com/documentation/ExternalAccessory/EASession) between your app and the device. Use that session to send commands to the device and retrieve data from it. You can also use the framework to detect when someone [`EAAccessoryManager`](https://developer.apple.com/documentation/ExternalAccessory/EAAccessoryManager#Managing-Connection-Status-Changes) an accessory.

#### Build Drivers to Support Custom Hardware Features

Macs and iPads provide USB ports for connecting external devices, and some devices support other types of ports. When someone attaches a device to the computer, the system searches for a driver capable of communicating with that device. If you develop custom hardware, create a  () to tell the system what services your device offers and how to communicate with it.

To simplify driver development, Apple operating systems contain a set of default drivers capable of communicating with devices that adopt industry-standard protocols. If your device adopts only standard protocols, create a [`Implementing drivers, system extensions, and kexts`](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts#3616855) to specify the protocols it supports. If your device extends the basic features or adds custom protocols, add code to your dext to support those custom features.

Create dexts for your hardware using the DriverKit SDK, which includes the [`DriverKit`](https://developer.apple.com/documentation/DriverKit) framework and other frameworks for communicating with specific types of devices. The APIs in these frameworks manage data moving to and from a device. The DriverKit SDK offers support for a variety of protocols, including:

- [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit) or [`MIDIDriverKit`](https://developer.apple.com/documentation/MIDIDriverKit) protocols
- [`BlockStorageDeviceDriverKit`](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit) protocols
- [`NetworkingDriverKit`](https://developer.apple.com/documentation/NetworkingDriverKit) protocols
- [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit) or [`HIDDriverKit`](https://developer.apple.com/documentation/HIDDriverKit) protocols
- [`PCIDriverKit`](https://developer.apple.com/documentation/PCIDriverKit) protocols
- SCSI [`SCSIControllerDriverKit`](https://developer.apple.com/documentation/SCSIControllerDriverKit) or [`SCSIPeripheralsDriverKit`](https://developer.apple.com/documentation/SCSIPeripheralsDriverKit) protocols
- [`SerialDriverKit`](https://developer.apple.com/documentation/SerialDriverKit) protocols, including ones over [`USBSerialDriverKit`](https://developer.apple.com/documentation/USBSerialDriverKit)

On Mac, you ship drivers as part of an app and [`Installing System Extensions and Drivers`](https://developer.apple.com/documentation/SystemExtensions/installing-system-extensions-and-drivers) from your code using the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework. On iPad, the system automatically scans for dexts in your app and loads them on demand. Because drivers interact with the kernel, your dexts must contain [`Requesting Entitlements for DriverKit Development`](https://developer.apple.com/documentation/DriverKit/requesting-entitlements-for-driverkit-development) for the system to run them.

> ❗ **Important**: Create [`Implementing drivers, system extensions, and kexts`](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts#3616855) instead of writing custom driver code whenever possible. Write custom driver code only to support features that are unique to your hardware, and debug your code thoroughly to eliminate crashes. Even minor bugs in drivers can prevent apps from communicating with your hardware or cause other issues.

#### Build Apps Specifically for Apple Silicon

Apple devices with [`Apple silicon`](https://developer.apple.com/documentation/apple-silicon) integrate the CPU, GPU, Apple Neural Engine (ANE), and memory into a single chip. Apple silicon is available on all Apple devices, making it easy to share code written for one device on other devices.

When building iOS apps, remember that your app can [`Running your iOS apps in macOS`](https://developer.apple.com/documentation/Apple-Silicon/running-your-ios-apps-in-macos). To create a better experience for people using your app, [`Adapting iOS code to run in the macOS environment`](https://developer.apple.com/documentation/Apple-Silicon/adapting-ios-code-to-run-in-the-macos-environment) to support menus and other features that iPad and Mac use regularly.

If you still have code that runs on Intel-based Macs, [`Porting your macOS apps to Apple silicon`](https://developer.apple.com/documentation/Apple-Silicon/porting-your-macos-apps-to-apple-silicon) to run on Apple silicon. Xcode makes it easy to recompile your code for Apple silicon, but you might need to [`Addressing architectural differences in your macOS code`](https://developer.apple.com/documentation/Apple-Silicon/addressing-architectural-differences-in-your-macos-code) you made about the underlying hardware architecture when writing your original code.

When performance is absolutely crucial, [`Tuning your code’s performance for Apple silicon`](https://developer.apple.com/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon) specifically for Apple silicon. Make sure you’re running the right code and taking advantage of parallel execution when you can. Review the [`Apple Silicon CPU Optimization Guide Version 4`](https://developer.apple.com/documentation/Apple-Silicon/cpu-optimization-guide) to make sure you’re not writing code in a way that hampers performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/hardware-level-interactions)*