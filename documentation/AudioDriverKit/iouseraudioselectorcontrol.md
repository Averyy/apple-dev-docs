# IOUserAudioSelectorControl

**Framework**: AudioDriverKit  
**Kind**: class

A control object that supports selecting from a set of values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioSelectorControl;
```

## Topics

### Creating a Selector Control
- [Create](iouseraudioselectorcontrol/create.md)
  Allocates and initializes an instance of the selector control class.
- [init](iouseraudioselectorcontrol/init.md)
  Initializes an instance of a selector control.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
### Freeing a Selector Control
- [free](iouseraudioselectorcontrol/free.md)
  Frees the selector control.
### Getting Information About the Class
- [GetClassID](iouseraudioselectorcontrol/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudioselectorcontrol/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Value Changes
- [HandleChangeSelectedValues](iouseraudioselectorcontrol/handlechangeselectedvalues.md)
  Tells the selection control the value is changing.
### Accessing the Selected Values
- [SetCurrentSelectedValues](iouseraudioselectorcontrol/setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](iouseraudioselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selections of the selector.
- [GetControlValuesCount](iouseraudioselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector values.
- [IOUserAudioSelectorValue](iouseraudioselectorvalue.md)
  The type of values managed by a selector control.
- [AddControlValueDescriptions](iouseraudioselectorcontrol/addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouseraudioselectorcontrol/removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [GetControlValueDescriptions](iouseraudioselectorcontrol/getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.

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
- [IOUserAudioLevelControl](iouseraudiolevelcontrol.md)
  A control object that supports setting an audio level, with either scalar or decibel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol)*