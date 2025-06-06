# IOUSBGetEndpointMaxPacketSize(_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the maximum packet size from an endpoint descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetEndpointMaxPacketSize(_ usbDeviceSpeed: UInt32, _ descriptor: UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt16
```

#### Return Value

The maximum packet size in bytes.

#### Discussion

This method parses an endpoint descriptor to determine its maximum packet size, which doesn’t include mult or burst factors.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The endpoint descriptor to parse.

## See Also

- [func IOUSBGetNextEndpointDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBInterfaceDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBEndpointDescriptor>!](iousbgetnextendpointdescriptor(_:_:_:).md)
  Obtains the next endpoint descriptor for an interface descriptor.
- [func IOUSBGetEndpointDirection(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointdirection(_:).md)
  Obtains the direction of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointAddress(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointaddress(_:).md)
  Obtains the direction and number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointNumber(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointnumber(_:).md)
  Obtains the number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointtype(_:).md)
  Obtains the type of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointIntervalEncodedMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalencodedmicroframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalmicroframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalFrames(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](iousbgetendpointintervalframes(_:_:).md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointMaxStreamsEncoded(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](iousbgetendpointmaxstreamsencoded(_:_:_:).md)
  Obtains the number of streams that an endpoint supports.
- [func IOUSBGetEndpointMaxStreams(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](iousbgetendpointmaxstreams(_:_:_:).md)
  Obtains the number of supported streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetendpointmaxpacketsize(_:_:))*