# IOUserAudioStereoPanControl

**Framework**: AudioDriverKit  
**Kind**: class  
**Role**: Class

A control object that supports panning between stereo channels.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
class IOUserAudioStereoPanControl;
```

## Topics

### Creating a Stereo Pan Control
- [Create](./iouseraudiostereopancontrol/create.md)
  Allocates and initializes an instance of the stereo pan control class.
- [init](./iouseraudiostereopancontrol/init.md)
  Initializes an instance of a stereo pan control.
- [IOUserAudioDriver](./iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](./audiodriverkit-page/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](./audiodriverkit-page/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
### Freeing a Stereo Pan Control
- [free](./iouseraudiostereopancontrol/free.md)
  Frees the stereo pan control.
### Getting Information About the Class
- [GetClassID](./iouseraudiostereopancontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](./iouseraudiostereopancontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](./audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Value Changes
- [HandleChangeControlValue](./iouseraudiostereopancontrol/handlechangecontrolvalue.md)
  Tells the stereo pan control the value is changing.
### Accessing the Value
- [SetControlValue](./iouseraudiostereopancontrol/setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [GetControlValue](./iouseraudiostereopancontrol/getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [SetPanningChannels](./iouseraudiostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.
- [GetPanningChannels](./iouseraudiostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.

## Relationships

### Inherits From
- [IOUserAudioControl](./iouseraudiocontrol.md)

## See Also

### Using Audio Controls
- [IOUserAudioControl](./iouseraudiocontrol.md)
  The base class for audio control objects.
- [IOUserAudioBooleanControl](./iouseraudiobooleancontrol.md)
  A control object that supports setting a Boolean value.
- [IOUserAudioSliderControl](./iouseraudioslidercontrol.md)
  A control object that supports setting a 32-bit integer value.
- [IOUserAudioSelectorControl](./iouseraudioselectorcontrol.md)
  A control object that supports selecting from a set of values.
- [IOUserAudioLevelControl](./iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol)*