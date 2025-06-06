# IOUserAudioLevelControl

**Framework**: AudioDriverKit  
**Kind**: class

A control object that supports setting an audio level, with either scalar or decibel values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioLevelControl;
```

## Topics

### Creating a Level Control
- [Create](iouseraudiolevelcontrol/create.md)
  Allocates and initializes an instance of the level control class.
- [init](iouseraudiolevelcontrol/init.md)
  Initializes an instance of a level control.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioLevelControlRange](iouseraudiolevelcontrolrange.md)
  A type that indicates minimum and maximum values for level controls.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
### Freeing a Level Control
- [free](iouseraudiolevelcontrol/free.md)
  Frees the level control.
### Getting Information About the Class
- [GetClassID](iouseraudiolevelcontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiolevelcontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Value Changes
- [HandleChangeScalarValue](iouseraudiolevelcontrol/handlechangescalarvalue.md)
  Tells the slider control the scalar value is changing.
- [HandleChangeDecibelValue](iouseraudiolevelcontrol/handlechangedecibelvalue.md)
  Tells the slider control the decibel value is changing.
### Accessing the Value
- [SetScalarValue](iouseraudiolevelcontrol/setscalarvalue.md)
  Sets the scalar value of the level control.
- [GetScalarValue](iouseraudiolevelcontrol/getscalarvalue.md)
  Gets the scalar value of the level control.
- [SetDecibelValue](iouseraudiolevelcontrol/setdecibelvalue.md)
  Sets the decibel value of the level control.
- [GetDecibelValue](iouseraudiolevelcontrol/getdecibelvalue.md)
  Gets the decibel value of the level control.

## Relationships

### Inherits From
- [IOUserAudioControl](iouseraudiocontrol.md)

## See Also

- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.
- [IOUserAudioBooleanControl](iouseraudiobooleancontrol.md)
  A control object that supports setting a Boolean value.
- [IOUserAudioStereoPanControl](iouseraudiostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserAudioSliderControl](iouseraudioslidercontrol.md)
  A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol)*