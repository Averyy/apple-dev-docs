# HIDVirtualDevice.Properties

**Framework**: Core HID  
**Kind**: struct  
**Role**: Structure

The properties for a virtual HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct Properties
```

## Mentions

- [Creating virtual devices](../creatingvirtualdevices.md)

#### Overview

A virtual device has many properties, required and optional, that determine or alter its functionality. Use this class to provide these properties during the creation of a virtual device.

Uncommon properties that aren’t available can be specified in the `extraProperties` parameter of [`init(descriptor:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:extraProperties:)`](./properties/init%28descriptor,vendorid,productid,transport,product,manufacturer,modelnumber,versionnumber,serialnumber,uniqueid,locationid,localizationcode,extraproperties%29.md).

## Topics

### Initializers
- [init(descriptor: Data, vendorID: UInt32, productID: UInt32?, transport: HIDDeviceTransport?, product: String?, manufacturer: String?, modelNumber: String?, versionNumber: UInt64?, serialNumber: String?, uniqueID: String?, locationID: UInt64?, localizationCode: HIDDeviceLocalizationCode?, extraProperties: Dictionary<String, AnyObject>?)](./properties/init%28descriptor,vendorid,productid,transport,product,manufacturer,modelnumber,versionnumber,serialnumber,uniqueid,locationid,localizationcode,extraproperties%29.md)
  Creates a set of properties for a virtual device.
### Instance Properties
- [let descriptor: Data](./properties/descriptor.md)
  The HID specification compliant report descriptor for the virtual device.
- [let localizationCode: HIDDeviceLocalizationCode?](./properties/localizationcode.md)
  A device localization code that specifies the HID compliant localization code.
- [let locationID: UInt64?](./properties/locationid.md)
  The location ID for the device.
- [let manufacturer: String?](./properties/manufacturer.md)
  The manufacturer of the device.
- [let modelNumber: String?](./properties/modelnumber.md)
  The model number for the device.
- [let product: String?](./properties/product.md)
  The product name for the device.
- [let productID: UInt32?](./properties/productid.md)
  The product ID for the device.
- [let serialNumber: String?](./properties/serialnumber.md)
  The serial number for the device.
- [let transport: HIDDeviceTransport?](./properties/transport.md)
  The data transport for the device.
- [let uniqueID: String?](./properties/uniqueid.md)
  A unique ID for the device.
- [let vendorID: UInt32](./properties/vendorid.md)
  The vendor ID for the device.
- [let versionNumber: UInt64?](./properties/versionnumber.md)
  The version of the device.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Simulation
- [Creating virtual devices](../creatingvirtualdevices.md)
  Use and interact with a virtual human interface device for testing and development.
- [actor HIDVirtualDevice](../hidvirtualdevice.md)
  A virtual service to emulate a HID device connected to the system.
- [protocol HIDVirtualDeviceDelegate](../hidvirtualdevicedelegate.md)
  The delegate to receive notifications for a virtual HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties)*