# SetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Set the transport type of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetTransportType(IOUserAudioTransportType in_transport_type);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

You can change the transport type dynamically. If the change succeeds, the framework sends a notification to the host to update its object state.

## Parameters

- `in_transport_type`: The audio transport type to set.

## See Also

- [GetTransportType](iouseraudiodriver/gettransporttype.md)
  Gets the transport type of the driver.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/settransporttype)*