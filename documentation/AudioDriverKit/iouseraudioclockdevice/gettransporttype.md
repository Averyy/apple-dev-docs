# GetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Gets the transport type of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioTransportType GetTransportType();
```

#### Return Value

The clock device’s transport type.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetTransportType](iouseraudioclockdevice/settransporttype.md)
  Sets the transport type of the clock device.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/gettransporttype)*