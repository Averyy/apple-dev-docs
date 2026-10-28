# GetTransportType

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the box’s transport type.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioTransportType GetTransportType();
```

## Return Value

The audio box’s `IOUserAudioTransportType`.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Transport Types
- [SetTransportType](./settransporttype.md)
  Sets the box’s transport type.
- [IOUserAudioTransportType](../audiodriverkit-page/iouseraudiotransporttype.md)
  The type of transport to deliver audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/gettransporttype)*