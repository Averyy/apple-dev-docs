# IOUserAudioSliderControl

**Framework**: AudioDriverKit  
**Kind**: class

A control object that supports setting a 32-bit integer value.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioSliderControl;
```

## Topics

### Creating a Slider Control
- [Create](iouseraudioslidercontrol/create.md)
  Allocates and initializes an instance of the slider control class.
- [init](iouseraudioslidercontrol/init.md)
  Initializes an instance of a slider control.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
### Freeing a Slider Control
- [free](iouseraudioslidercontrol/free.md)
  Frees the slider control.
### Getting Information About the Class
- [GetClassID](iouseraudioslidercontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudioslidercontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Value Changes
- [HandleChangeControlValue](iouseraudioslidercontrol/handlechangecontrolvalue.md)
  Tells the slider control the value is changing.
### Accessing the Value
- [SetControlValue](iouseraudioslidercontrol/setcontrolvalue.md)
  Sets the value of the slider control.
- [GetControlValue](iouseraudioslidercontrol/getcontrolvalue.md)
  Gets the value of the slider control.
- [SetRange](iouseraudioslidercontrol/setrange.md)
  Sets the range of possible values for the slider.
- [GetRange](iouseraudioslidercontrol/getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.

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
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol)*