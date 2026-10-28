# IOUSBGetEndpointMaxStreamsEncoded(_:_:_:)

**Framework**: IOUSBHost  
**Kind**: func  
**Role**: Function

Obtains the number of streams that an endpoint supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func IOUSBGetEndpointMaxStreamsEncoded(_ usbDeviceSpeed: UInt32, _ descriptor: UnsafePointer<IOUSBEndpointDescriptor>!, _ companionDescriptor: UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32
```

```c
uint32_t IOUSBGetEndpointMaxStreamsEncoded(uint32_t usbDeviceSpeed, const IOUSBEndpointDescriptor *descriptor, const IOUSBSuperSpeedEndpointCompanionDescriptor *companionDescriptor);
```

## Return Value

The encoded number of streams.

## Discussion

This method parses endpoint descriptors and returns the number of supported streams as *n* in *(2^n)*.

## Parameters

- `usbDeviceSpeed`: The operational speed of the device.
- `descriptor`: The endpoint descriptor to parse.
- `companionDescriptor`: The companion descriptor to parse.

## See Also

### Endpoint Descriptor Parsing
- [func IOUSBGetNextEndpointDescriptor(UnsafePointer<IOUSBConfigurationDescriptor>!, UnsafePointer<IOUSBInterfaceDescriptor>!, UnsafePointer<IOUSBDescriptorHeader>!) -> UnsafePointer<IOUSBEndpointDescriptor>!](./iousbgetnextendpointdescriptor%28_,_,_%29.md)
  Obtains the next endpoint descriptor for an interface descriptor.
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
- [func IOUSBGetEndpointMaxStreams(UInt32, UnsafePointer<IOUSBEndpointDescriptor>!, UnsafePointer<IOUSBSuperSpeedEndpointCompanionDescriptor>!) -> UInt32](./iousbgetendpointmaxstreams%28_,_,_%29.md)
  Obtains the number of supported streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbgetendpointmaxstreamsencoded(_:_:_:))*