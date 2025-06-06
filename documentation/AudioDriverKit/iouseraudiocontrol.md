# IOUserAudioControl

**Framework**: AudioDriverKit  
**Kind**: class

The base class for audio control objects.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioControl;
```

#### Overview

Don’t subclass or allocate this class directly.

## Topics

### Creating a Control
- [init](iouseraudiocontrol/init.md)
  Initializes an instance of an audio control.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
### Freeing a Control
- [free](iouseraudiocontrol/free.md)
  Frees the audio control.
### Getting Information About the Class
- [GetClassID](iouseraudiocontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiocontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Working with Control Properties
- [GetControlScope](iouseraudiocontrol/getcontrolscope.md)
  Returns the control’s scope: input, output, global, or play-through.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [GetControlElement](iouseraudiocontrol/getcontrolelement.md)
  Returns the control’s identifying element.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyElementMain](audiodriverkit/iouseraudioobjectpropertyelementmain.md)
  The identifier for an audio object’s main element.
- [GetIsSettable](iouseraudiocontrol/getissettable.md)
  Returns a Boolean value that idicates if the control can be set.

## Relationships

### Inherits From
- [IOUserAudioObject](iouseraudioobject.md)
### Inherited By
- [IOUserAudioBooleanControl](iouseraudiobooleancontrol.md)
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
- [IOUserAudioSliderControl](iouseraudioslidercontrol.md)
- [IOUserAudioStereoPanControl](iouseraudiostereopancontrol.md)

## See Also

- [IOUserAudioBooleanControl](iouseraudiobooleancontrol.md)
  A control object that supports setting a Boolean value.
- [IOUserAudioStereoPanControl](iouseraudiostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserAudioSliderControl](iouseraudioslidercontrol.md)
  A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocontrol)*