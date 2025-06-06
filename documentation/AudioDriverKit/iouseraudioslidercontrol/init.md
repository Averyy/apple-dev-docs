# init

**Framework**: AudioDriverKit  
**Kind**: method

Initializes an instance of a slider control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool init(IOUserAudioDriver * in_driver, bool in_is_settable, uint32_t in_control_value, IOUserAudioSliderRange in_range, IOUserAudioObjectPropertyElement in_control_element, IOUserAudioObjectPropertyScope in_control_scope, IOUserAudioClassID in_control_class_id);
```

#### Return Value

`true` if initialization succeeded; `false` otherwise.

## Parameters

- `in_driver`: The   that owns this object.
- `in_is_settable`: A Boolean value that indicates if the control can be set.
- `in_control_value`: A   value that represents the control’s current value.
- `in_range`: The range that defines minimum and maximum values for the slider.
- `in_control_element`: An   to identify the control.
- `in_control_scope`: A   indicating the control’s scope: input, output, global, or play-through.
- `in_control_class_id`: The   of the control.

## See Also

- [Create](iouseraudioslidercontrol/create.md)
  Allocates and initializes an instance of the slider control class.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/init)*