# GetTransportType

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the transport type of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioTransportType GetTransportType();
```

#### Return Value

The clock device’s transport type.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Transport Type
- [SetTransportType](./settransporttype.md)
  Sets the transport type of the clock device.
- [IOUserAudioTransportType](../audiodriverkit-page/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/gettransporttype)*