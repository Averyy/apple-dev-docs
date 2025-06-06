# GetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Returns the box’s transport type.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioTransportType GetTransportType();
```

#### Return Value

The audio box’s `IOUserAudioTransportType`.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetTransportType](iouseraudiobox/settransporttype.md)
  Sets the box’s transport type.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/gettransporttype)*