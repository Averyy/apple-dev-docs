# GetTransportType

**Framework**: AudioDriverKit  
**Kind**: method

Gets the transport type of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioTransportType GetTransportType();
```

#### Return Value

The transport type of the driver.

#### Discussion

Getting the value synchronizes by using the work queue created by the object.

## See Also

- [SetTransportType](iouseraudiodriver/settransporttype.md)
  Set the transport type of the driver.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/gettransporttype)*