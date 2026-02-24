# init

**Framework**: AudioDriverKit  
**Kind**: method

Initializes an instance of an audio control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
virtual bool init(IOUserAudioDriver *in_driver, bool in_is_settable, IOUserAudioObjectPropertyElement in_control_element, IOUserAudioObjectPropertyScope in_control_scope);
```

#### Return Value

`true` if initialization succeeded; `false` otherwise.

## Parameters

- `in_driver`: The [`IOUserAudioDriver`](iouseraudiodriver.md) that owns this object.
- `in_is_settable`: A Boolean value that indicates if the control can be set.
- `in_control_element`: An [`IOUserAudioObjectPropertyElement`](audiodriverkit/iouseraudioobjectpropertyelement.md) to identify the control.
- `in_control_scope`: A [`IOUserAudioObjectPropertyScope`](audiodriverkit/iouseraudioobjectpropertyscope.md) indicating the control’s scope: input, output, global, or play-through.

## See Also

- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocontrol/init)*