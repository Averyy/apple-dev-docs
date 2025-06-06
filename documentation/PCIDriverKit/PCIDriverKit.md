# PCIDriverKit

**Framework**: PCIDriverKit  
**Kind**: module

Develop device drivers for Peripheral Component Interconnect (PCI) accessories.

**Availability**:
- DriverKit 19.0+
- macOS 11.1+

## Mentions

- [Creating Custom PCIe Drivers for Thunderbolt Devices](creating-custom-pcie-drivers-for-thunderbolt-devices.md)

#### Overview

Use the PCIDriverKit framework to develop drivers that manage custom features on your Peripheral Component Interconnect (PCI) and PCI-Express hardware. When the system loads your custom PCI driver, it passes an [`IOPCIDevice`](iopcidevice.md) object as the provider to your driver. Use that object to read and write the configuration and memory of your PCI hardware.

On macOS, use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> **Note**:  PCIDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series chip.

 PCIDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series chip.

## Topics

### Entitlements
- [com.apple.developer.driverkit.transport.pci](../BundleResources/Entitlements/com.apple.developer.driverkit.transport.pci.md)
  An array of PCI device descriptors that your custom driver supports.
### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Device Interface
- [Creating Custom PCIe Drivers for Thunderbolt Devices](creating-custom-pcie-drivers-for-thunderbolt-devices.md)
  Create a DriverKit extension to support your Thunderbolt device’s custom features.
- [IOPCIDevice](iopcidevice.md)
  A DriverKit provider object that manages access to your custom PCI hardware.
### Reference
- [PCIDriverKit Enumerations](pcidriverkit-enumerations.md)
- [PCIDriverKit Data Types](pcidriverkit-data-types.md)
- [PCIDriverKit Macros](pcidriverkit-macros.md)
### Enumeration Cases
- [kIOPCISlotStatusAttentionButtonPressed](kiopcislotstatusattentionbuttonpressed.md)
- [kIOPCISlotStatusCommandCompleted](kiopcislotstatuscommandcompleted.md)
- [kIOPCISlotStatusDataLinkLayerStateChanged](kiopcislotstatusdatalinklayerstatechanged.md)
- [kIOPCISlotStatusElectromechanicalInterlockState](kiopcislotstatuselectromechanicalinterlockstate.md)
- [kIOPCISlotStatusMRLSensorChanged](kiopcislotstatusmrlsensorchanged.md)
- [kIOPCISlotStatusMRLSensorState](kiopcislotstatusmrlsensorstate.md)
- [kIOPCISlotStatusPowerFaultDetected](kiopcislotstatuspowerfaultdetected.md)
- [kIOPCISlotStatusPresenceDetectChanged](kiopcislotstatuspresencedetectchanged.md)
- [kIOPCISlotStatusPresenceDetectState](kiopcislotstatuspresencedetectstate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/PCIDriverKit)*