# GetClassID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the audio class identifier of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual IOUserAudioClassID GetClassID();
```

#### Return Value

The audio class identifier of the object.

#### Discussion

This method overrides the base class [`IOUserAudioObject`](../iouseraudioobject.md).

## See Also

### Getting Information About the Class
- [GetBaseClassID](./getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobooleancontrol/getclassid)*