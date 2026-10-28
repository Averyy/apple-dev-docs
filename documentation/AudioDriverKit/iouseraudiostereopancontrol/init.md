# init

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes an instance of a stereo pan control.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual bool init(IOUserAudioDriver *in_driver, bool in_is_settable, float in_control_value, IOUserAudioObjectPropertyElement in_left_channel, IOUserAudioObjectPropertyElement in_right_channel, IOUserAudioObjectPropertyElement in_control_element, IOUserAudioObjectPropertyScope in_control_scope, IOUserAudioClassID in_control_class_id);
```

## Return Value

`true` if initialization succeeded; `false` otherwise.

## Parameters

- `in_driver`: The [`IOUserAudioDriver`](../iouseraudiodriver.md) that owns this object.
- `in_is_settable`: A Boolean value that indicates if the control can be set.
- `in_control_value`: A floating-point value that represents the control’s current stereo pan value.
- `in_left_channel`: The [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the left channel.
- `in_right_channel`: The [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the right channel.
- `in_control_element`: An [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) to identify the control.
- `in_control_scope`: A [`IOUserAudioObjectPropertyScope`](../audiodriverkit-page/iouseraudioobjectpropertyscope.md) indicating the control’s scope: input, output, global, or play-through.
- `in_control_class_id`: The [`IOUserAudioClassID`](../audiodriverkit-page/iouseraudioclassid.md) of the control.

## See Also

### Creating a Stereo Pan Control
- [Create](./create.md)
  Allocates and initializes an instance of the stereo pan control class.
- [IOUserAudioDriver](../iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](../audiodriverkit-page/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](../audiodriverkit-page/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/init)*