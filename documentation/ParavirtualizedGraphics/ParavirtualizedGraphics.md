# Paravirtualized Graphics

**Framework**: Paravirtualized Graphics  
**Kind**: module

Add graphics acceleration to your guest driver stack.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

#### Overview

If you have an app that implements hardware-level virtualization, performance inside the virtual machine is critical, particularly for graphics. The ParavirtualizedGraphics framework implements hardware-accelerated graphics for macOS running in a virtual machine, hereafter known as the guest. The operating system provides a graphics driver that runs inside the guest, communicating with the framework in the host operating system to take advantage of Metal-accelerated graphics.

To implement accelerated graphics inside your virtualization solution, you need to take the following steps for each virtual machine:

1. Advertise the virtual graphics card in the virtual machine hardware so that macOS can install the correct driver.
2. Create a [`PGDeviceDescriptor`](pgdevicedescriptor.md), providing the necessary blocks to connect your virtual machine implementation to the ParavirtualizedGraphics framework. Use this descriptor to create a [`PGDevice`](pgdevice.md) object, which you keep alive as long as the virtual machine is still active. The ParavirtualizedGraphics framework calls your blocks when it needs to allocate memory or take other relevant actions.
3. Create a [`PGDisplayDescriptor`](pgdisplaydescriptor.md) for each virtual display that you want to connect to the device, specifying the display’s properties and blocks for the framework to call for display events. Use this descriptor to create a [`PGDisplay`](pgdisplay.md) object. Handle the appropriate display events to display the graphics data that the framework provides.

## Topics

### PCI Device Characteristics
- [var PG_PCI_DEVICE_ID: Int32](pg_pci_device_id.md)
  The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_VENDOR_ID: Int32](pg_pci_vendor_id.md)
  The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_BAR_MMIO: Int32](pg_pci_bar_mmio.md)
  The base address register to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_MAX_MSI_VECTORS: Int32](pg_pci_max_msi_vectors.md)
  The number of MSI vectors that you need to allocate for the graphics configuration.
- [func PGCopyOptionROMURL() -> URL](pgcopyoptionromurl().md)
  Copies the URL of the ROM image to use on the guest graphics device.
### Devices
- [func PGNewDeviceWithDescriptor(PGDeviceDescriptor) -> (any PGDevice)?](pgnewdevicewithdescriptor(_:).md)
  Creates a new paravirtualized graphics device.
- [class PGDeviceDescriptor](pgdevicedescriptor.md)
  A description of the paravirtualized graphics device to create.
- [protocol PGDevice](pgdevice.md)
  A paravirtualized GPU device object.
### Displays
- [class PGDisplayDescriptor](pgdisplaydescriptor.md)
  A descriptor for a virtual display.
- [protocol PGDisplay](pgdisplay.md)
  An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- [class PGDisplayMode](pgdisplaymode.md)
  A description of a supported display mode.
- [struct PGDisplayCoord_t](pgdisplaycoord_t.md)
  Coordinates that describe sizes or offsets within a 2D array of pixels.
### Reference
- [ParavirtualizedGraphics Constants](paravirtualizedgraphics-constants.md)
- [ParavirtualizedGraphics Functions](paravirtualizedgraphics-functions.md)
- [ParavirtualizedGraphics Data Types](paravirtualizedgraphics-data-types.md)
### Variables
- [var HAS_NS_BITMAP_HEADER: Int32](has_ns_bitmap_header.md)
- [var PG_SUPPORT_CREATE_DEVICE: Int32](pg_support_create_device.md)
### Functions
- [func PGCreateDeviceWithDescriptor(PGDeviceDescriptor) -> (any PGDevice)?](pgcreatedevicewithdescriptor(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ParavirtualizedGraphics)*