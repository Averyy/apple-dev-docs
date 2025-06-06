# IOUserAudioBooleanControl

**Framework**: AudioDriverKit  
**Kind**: class

A control object that supports setting a Boolean value.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioBooleanControl;
```

## Topics

### Creating a Boolean Control
- [Create](iouseraudiobooleancontrol/create.md)
  Allocates and initializes an instance of the Boolean control class.
- [init](iouseraudiobooleancontrol/init.md)
  Initializes an instance of a Boolean control.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
### Freeing a Boolean Control
- [free](iouseraudiobooleancontrol/free.md)
  Frees the audio Boolean control.
### Getting Information About the Class
- [GetClassID](iouseraudiobooleancontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiobooleancontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Value Changes
- [HandleChangeControlValue](iouseraudiobooleancontrol/handlechangecontrolvalue.md)
  Tells the Boolean control the value is changing.
### Accessing the Value
- [SetControlValue](iouseraudiobooleancontrol/setcontrolvalue.md)
  Sets the Boolean value of the control.
- [GetControlValue](iouseraudiobooleancontrol/getcontrolvalue.md)
  Gets the Boolean value of the control.

## Relationships

### Inherits From
- [IOUserAudioControl](iouseraudiocontrol.md)

## See Also

- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.
- [IOUserAudioStereoPanControl](iouseraudiostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserAudioSliderControl](iouseraudioslidercontrol.md)
  A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobooleancontrol)*