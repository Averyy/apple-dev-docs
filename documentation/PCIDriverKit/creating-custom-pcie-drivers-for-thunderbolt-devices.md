# Creating Custom PCIe Drivers for Thunderbolt Devices

**Framework**: PCIDriverKit

Create a DriverKit extension to support your Thunderbolt device’s custom features.

#### Overview

All hardware devices require special software — called drivers — to communicate with macOS. Thunderbolt devices communicate using the PCIe interface, and so they use PCIe drivers with extra support for Thunderbolt features.

If your Thunderbolt device uses popular PCIe Ethernet controllers from Intel, Broadcom, or Aquantia, or if your device communicates using industry-standard protocols such as XHCI, AHCI, NVMe, or FireWire, you don’t need to create a custom driver. Apple supplies built-in drivers that already support these chip sets and interfaces. The only time you need to create a custom driver is when your hardware supports proprietary features. In macOS 11 and later, build any custom drivers as DriverKit extensions using the [`PCIDriverKit`](PCIDriverKit.md) framework.

> **Note**:  If your Thunderbolt device requires capabilities that DriverKit doesn’t support, such as manipulating audio or communicating wirelessly over Bluetooth or Wi-Fi, create your driver as an IOKit kernel extension instead. For more information, see [`Implementing a PCIe Kext for a Thunderbolt Device`](https://developer.apple.com/documentation/kernel/hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device).

 If your Thunderbolt device requires capabilities that DriverKit doesn’t support, such as manipulating audio or communicating wirelessly over Bluetooth or Wi-Fi, create your driver as an IOKit kernel extension instead. For more information, see [`Implementing a PCIe Kext for a Thunderbolt Device`](https://developer.apple.com/documentation/kernel/hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device).

For basic information on how to create a DriverKit extension, see [`Creating a Driver Using the DriverKit SDK`](https://developer.apple.com/documentation/DriverKit/creating-a-driver-using-the-driverkit-sdk).

##### Request the Entitlements Required to Run Your Driver

The system requires every DriverKit driver to have an appropriate set of entitlements. Drivers interact with sensitive parts of the system, including the kernel and attached hardware peripherals. Entitlements protect those resources by ensuring that only authorized drivers communicate with them. Specifically, the system prevents drivers from accessing resources for which they don’t have the appropriate entitlements.

Drivers for Thunderbolt devices must have the following entitlements:

- [`com.apple.developer.driverkit`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit)
- [`com.apple.developer.driverkit.transport.pci`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.pci)

You request DriverKit entitlements directly from Apple, which adds the entitlements to your developer account. You then add those entitlements to your Xcode project, and to the provisioning profile you use to cryptographically sign your app. For information about how to request DriverKit entitlements and add them to your Xcode project, see [`Requesting Entitlements for DriverKit Development`](https://developer.apple.com/documentation/DriverKit/requesting-entitlements-for-driverkit-development).

##### Add Thunderbolt Support to Your Drivers Personality Data

When it detects new hardware, the system must find an appropriate set of drivers to manage that hardware. It does so by comparing the hardware details to information found in the `kIOKitPersonalitiesKey` key of each driver’s `Info.plist` file, and identifying the drivers that best match the hardware. For example, a driver might match only against devices from a specific manufacturer, or devices that support only a specific communication protocol.

To indicate that your PCIe driver supports Thunderbolt, include the `IOPCITunnelCompatible` key in your driver’s personality dictionaries. Include this key only if the [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass in the `IOClass` key of that dictionary is able to communicate with your Thunderbolt device. The following example shows the presence of this key in a custom PCI driver.

```other
<key>MyDriverKitDriver</key>
<dict>
    <key>CFBundleIdentifier</key>
    <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
    <key>CFBundleIdentifierKernel</key>
    <string>com.apple.kpi.iokit</string>
    <key>IOClass</key>
    <string>IOUserService</string>
    <key>IOPCIPauseCompatible</key>
    <true/>
    <key>IOPCIPrimaryMatch</key>
    <string>0x0000ABCD&amp;0x0000FFFF</string>
    <key>IOPCITunnelCompatible</key>
    <true/>
    <key>IOProviderClass</key>
    <string>IOPCIDevice</string>
    <key>IOResourceMatch</key>
    <string>IOKit</string>
    <key>IOUserClass</key>
    <string>MyPCIDriverKitDriverClassName</string>
    <key>IOUserServerName</key>
    <string>com.apple.MyDriverKitDriver</string>
</dict>
```

##### Notify the System of External Storage Devices

Users can disconnect most Thunderbolt devices at any time, but macOS doesn’t allow them to disconnect external storage devices without properly ejecting them. If your PCI driver presents the device as storage to the system, notify the system early in your driver’s [`Start`](https://developer.apple.com/documentation/kernel/ioservice/3180710-start) method by setting the `Physical Interconnect Location` property to `External`, as in the following example:

```objc
// Add the Physical Interconnect Location property to the driver.
OSDictionary* dict = OSDictionary::withCapacity(1);
OSString* externalStr = OSString::withCString("External");
dict->setObject("Physical Interconnect Location", externalStr);
SetProperties(dict);
OSSafeReleaseNULL(externalStr);
OSSafeReleaseNULL(dict);
```

> ❗ **Important**:  Always set the `Physical Interconnect Location` property early in your driver’s [`Start`](https://developer.apple.com/documentation/kernel/ioservice/3180710-start) method. Don’t set it after you access the device.

 Always set the `Physical Interconnect Location` property early in your driver’s [`Start`](https://developer.apple.com/documentation/kernel/ioservice/3180710-start) method. Don’t set it after you access the device.

##### Support Message Signaled Interrupts in Your Device

Always use Message Signaled Interrupts (MSI) to generate hardware interrupts from your Thunderbolt devices. You can implement a DriverKit extension with legacy interrupts, but doing so adds latency to any device that shares the interrupt. If you need to support legacy interrupts, the better alternative is to implement your driver as a kernel extension.

For MSI-enabled Thunderbolt devices, the system routes interrupts to the appropriate [`IOInterruptDispatchSource`](https://developer.apple.com/documentation/DriverKit/IOInterruptDispatchSource) object in your driver. Create and configure interrupt dispatch sources in the [`Start`](https://developer.apple.com/documentation/kernel/ioservice/3180710-start) method of your custom [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass. For more information, see [`IOInterruptDispatchSource`](https://developer.apple.com/documentation/kernel/iointerruptdispatchsource).

##### Read and Write From the Configuration and Mmio Spaces

Drivers communicate with a PCI device primarily through one of the following memory spaces:

- The  contains the registers that you use to manage the state of the device and its settings. For example, use these registers to configure the power management behavior of the device.
- The  (MMIO) space contains the device’s custom data. When your driver needs to interact with device-specific features, read or write in the MMIO space according to the device’s specifications.

> ❗ **Important**:  Older PCI devices may also support the I/O memory space, which is similar to the MMIO space. Macs with Apple silicon don’t support the I/O space, and Apple discourages the use of the I/O space in your devices or drivers. Instead, use the MMIO space for custom communication between your driver and device.

 Older PCI devices may also support the I/O memory space, which is similar to the MMIO space. Macs with Apple silicon don’t support the I/O space, and Apple discourages the use of the I/O space in your devices or drivers. Instead, use the MMIO space for custom communication between your driver and device.

For more information about the memory spaces to use in your drivers, see the PCI specification at [`https://pcisig.com`](https://developer.apple.comhttps://pcisig.com).

## See Also

- [IOPCIDevice](iopcidevice.md)
  A DriverKit provider object that manages access to your custom PCI hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/creating-custom-pcie-drivers-for-thunderbolt-devices)*