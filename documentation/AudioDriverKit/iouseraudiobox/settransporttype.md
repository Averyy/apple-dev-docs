# SetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Sets the box’s transport type.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetTransportType(IOUserAudioTransportType in_transport_type);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the transport type sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_transport_type`: The   to set for the audio box.

## See Also

- [GetTransportType](iouseraudiobox/gettransporttype.md)
  Returns the box’s transport type.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/settransporttype)*