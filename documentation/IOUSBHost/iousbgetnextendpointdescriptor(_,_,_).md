# IOUSBGetNextEndpointDescriptor(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the next endpoint descriptor for an interface descriptor.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetNextEndpointDescriptor(_ configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>!, _ interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>!, _ currentDescriptor: UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBEndpointDescriptor>!
```

```c
const IOUSBEndpointDescriptor *IOUSBGetNextEndpointDescriptor(const IOUSBConfigurationDescriptor *configurationDescriptor, const IOUSBInterfaceDescriptor *interfaceDescriptor, const IOUSBDescriptorHeader *currentDescriptor);
```

#### Return Value

A descriptor pointer, or `nil` if no matching descriptor returns.

#### Discussion

This method uses [`IOUSBGetNextAssociatedDescriptorWithType(_:_:_:_:)`](./iousbgetnextassociateddescriptorwithtype%28_,_,_,_%29.md) to find the next endpoint descriptor for a specific interface descriptor.

## Parameters

- `configurationDescriptor`: A configuration descriptor that contains the descriptors to iterate through.
- `interfaceDescriptor`: An interface descriptor within the bounds of `configurationDescriptor`.
- `currentDescriptor`: A descriptor pointer within the bounds of `configurationDescriptor`, or `nil`.

## See Also

### Endpoint Descriptor Parsing
- [func IOUSBGetEndpointDirection(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointdirection%28_%29.md)
  Obtains the direction of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointAddress(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointaddress%28_%29.md)
  Obtains the direction and number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointNumber(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointnumber%28_%29.md)
  Obtains the number of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointType(UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt8](./iousbgetendpointtype%28_%29.md)
  Obtains the type of an endpoint from an endpoint descriptor.
- [func IOUSBGetEndpointMaxPacketSize(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt16](./iousbgetendpointmaxpacketsize%28_,_%29.md)
  Obtains the maximum packet size from an endpoint descriptor.
- [func IOUSBGetEndpointIntervalEncodedMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](./iousbgetendpointintervalencodedmicroframes%28_,_%29.md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalMicroframes(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](./iousbgetendpointintervalmicroframes%28_,_%29.md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointIntervalFrames(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!) -> UInt32](./iousbgetendpointintervalframes%28_,_%29.md)
  Obtains the interval of an endpoint descriptor.
- [func IOUSBGetEndpointMaxStreamsEncoded(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](./iousbgetendpointmaxstreamsencoded%28_,_,_%29.md)
  Obtains the number of streams that an endpoint supports.
- [func IOUSBGetEndpointMaxStreams(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](./iousbgetendpointmaxstreams%28_,_,_%29.md)
  Obtains the number of supported streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetnextendpointdescriptor(_:_:_:))*