# IOPCIDevice

**Framework**: Pcidriverkit  
**Kind**: class

A DriverKit provider object that manages access to your custom PCI hardware.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOPCIDevice;
```

#### Overview

Use an `IOPCIDevice` object to enable or manage the custom features of your PCI hardware. You don’t create instances of this class directly. Instead, the system creates an `IOPCIDevice` object and passes it to the [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) subclass of your custom driver. Use the methods of this object to read and write your hardware’s configuration settings. You can also use it to read and write any custom data in your device’s memory-mapped I/O.

> **Note**:  The endpoint driver is responsible for enabling the Memory Space Enable and Bus Master Enable settings each time it configures the PCI device. When a crash occurs, or when the system unloads your driver, the system disables these features.

## Topics

### Running the Service
- [init](iopcidevice/init.md)
  Initializes the device.
- [Open](iopcidevice/open.md)
  Opens a session to the PCI device.
- [Close](iopcidevice/close.md)
  Closes the session to the PCI device.
- [free](iopcidevice/free.md)
  Performs any final cleanup for the object.
### Reading and Writing Configuration Data
- [ConfigurationRead8](iopcidevice/configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead16](iopcidevice/configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead32](iopcidevice/configurationread32.md)
  Reads a 32-bit data value synchronously from the device’s configuration space.
- [ConfigurationWrite8](iopcidevice/configurationwrite8.md)
  Writes an 8-bit data value to the device’s configuration space.
- [ConfigurationWrite16](iopcidevice/configurationwrite16.md)
  Writes an 16-bit data value to the device’s configuration space.
- [ConfigurationWrite32](iopcidevice/configurationwrite32.md)
  Writes an 32-bit data value to the device’s configuration space.
- [Configuration Data Offsets](configuration-data-offsets-enum.md)
  Constants for the offsets that you use to read and write configuration registers.
- [Bridge Header Offsets](bridge-header-offsets-enum.md)
  Constants that specify offsets to distinct registers in a memory range.
- [Command Register Bits](command-register-bits-enum.md)
  Constants that you use to access specific bits of the command register.
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.
### Reading and Writing Memory Locations
- [MemoryRead8](iopcidevice/memoryread8-1edw0.md)
  Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead8](iopcidevice/memoryread8-7b2zp.md)
  Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead16](iopcidevice/memoryread16-9qkdh.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead16](iopcidevice/memoryread16-50bq8.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead32](iopcidevice/memoryread32-60hg9.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead32](iopcidevice/memoryread32-84jap.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead64](iopcidevice/memoryread64-9ntrf.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead64](iopcidevice/memoryread64-37uob.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryWrite8](iopcidevice/memorywrite8-1uey6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite8](iopcidevice/memorywrite8-fzh6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite16](iopcidevice/memorywrite16-8k6ch.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite16](iopcidevice/memorywrite16-534yk.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite32](iopcidevice/memorywrite32-4pmh.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite32](iopcidevice/memorywrite32-ow7r.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite64](iopcidevice/memorywrite64-8qyob.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite64](iopcidevice/memorywrite64-nvpu.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.
### Getting Device Information
- [FindPCICapability](iopcidevice/findpcicapability.md)
  Search the configuration space for a PCI capability register.
- [GetBusDeviceFunction](iopcidevice/getbusdevicefunction.md)
  Returns the device’s bus, device, and function numbers.
- [PCI Capabilities](pci-capabilities-enum.md)
  Constants that you use to get the capabilities of the PCI device.
- [Slot Capabilities](slot-capabilities-enum.md)
  Constants that you use to get the slot-related capabilities of the PCI device.
### Managing Interrupts
- [Interrupt Types](../kernel/1640325-interrupt_types.md)
  Interrupt types that the device supports.
### Managing Power
- [HasPCIPowerManagement](iopcidevice/haspcipowermanagement.md)
  Determines whether the device has the specified PCI bus power management capabilities.
- [EnablePCIPowerManagement](iopcidevice/enablepcipowermanagement.md)
  Configures the device’s PCI bus power management capabilities.
- [Power Management Capabilities](power-management-capabilities-enum.md)
  Constants you use to get and set the state of the device’s power management features.
- [Power Management Control/Status Register](power-management-control-status-register-enum.md)
  Constants you use when checking bits in the power management register.
### Getting Error Codes
- [Correctable Error Bits](correctable-error-bits-enum.md)
  Constants for the bits in the correctable error status register.
- [Uncorrectable Error Bits](uncorrectable-error-bits-enum.md)
  Constants for the bits in the uncorrectable error status register.
### Instance Methods
- [ClientCrashed](iopcidevice/clientcrashed.md)
- [ConfigureInterrupts](iopcidevice/configureinterrupts.md)
- [GetBARInfo](iopcidevice/getbarinfo.md)
- [GetLinkSpeed](iopcidevice/getlinkspeed.md)
- [Reset](iopcidevice/reset.md)
- [RestoreDeviceState](iopcidevice/restoredevicestate.md)
- [SaveDeviceState](iopcidevice/savedevicestate.md)
- [SetASPMState](iopcidevice/setaspmstate.md)
- [SetLinkSpeed](iopcidevice/setlinkspeed.md)
- [SetProperties](iopcidevice/setproperties.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [Creating Custom PCIe Drivers for Thunderbolt Devices](creating-custom-pcie-drivers-for-thunderbolt-devices.md)
  Create a DriverKit extension to support your Thunderbolt device’s custom features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PCIDriverKit/iopcidevice)*