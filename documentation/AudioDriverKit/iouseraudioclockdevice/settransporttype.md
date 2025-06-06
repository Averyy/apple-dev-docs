# SetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Sets the transport type of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetTransportType(IOUserAudioTransportType in_transport_type);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Drivers can change the transport type of the clock device dynamically. If successful, changing the transport type sends a notification to the host to update the object state.

## Parameters

- `in_transport_type`: The transport type to set.

## See Also

- [GetTransportType](iouseraudioclockdevice/gettransporttype.md)
  Gets the transport type of the clock device.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/settransporttype)*