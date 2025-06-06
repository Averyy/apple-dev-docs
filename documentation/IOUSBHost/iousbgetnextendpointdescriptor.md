# IOUSBGetNextEndpointDescriptor(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func

Obtains the next endpoint descriptor for an interface descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextEndpointDescriptor(_ configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>!, _ interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBEndpointDescriptor>!
```

#### Return Value

A descriptor pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextAssociatedDescriptorWithType(_:_:_:_:)`](iousbgetnextassociateddescriptorwithtype(_:_:_:_:).md) to find the next endpoint descriptor for a specific interface descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `interfaceDescriptor`: An interface descriptor within the bounds of  .
- `currentDescriptor`: A descriptor pointer within the bounds of  , or  .

## See Also

- [func IOUSBGetEndpointDirection(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointdirection(_:).md)
  Obtains the direction of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointAddress(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointaddress(_:).md)
  Obtains the direction and number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointNumber(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointnumber(_:).md)
  Obtains the number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](iousbgetendpointtype(_:).md)
  Obtains the type of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointMaxPacketSize(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt16](iousbgetendpointmaxpacketsize(_:_:).md)
  Obtains the maximum packet size from an endpoint descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextendpointdescriptor(_:_:_:))*