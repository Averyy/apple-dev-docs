# GetBaseClassID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the audio class identifier of the base class object.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual IOUserAudioClassID GetBaseClassID();
```

## Return Value

The audio class identifier of the base class object.

## Discussion

This method overrides the base class [`IOUserAudioObject`](../iouseraudioobject.md).

## See Also

### Getting Information About the Class
- [GetClassID](./getclassid.md)
  Gets the audio class identifier of the object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getbaseclassid)*