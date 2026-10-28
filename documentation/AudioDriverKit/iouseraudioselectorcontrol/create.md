# Create

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Static Method

Allocates and initializes an instance of the selector control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
static OSSharedPtr<IOUserAudioSelectorControl> Create(IOUserAudioDriver *in_driver, bool in_is_settable, IOUserAudioObjectPropertyElement in_control_element, IOUserAudioObjectPropertyScope in_control_scope, IOUserAudioClassID in_control_class_id);
```

## Return Value

A poiner to an [`IOUserAudioSelectorControl`](../iouseraudioselectorcontrol.md), if allocation and initialization succeeded.

## Discussion

If you subclass [`IOUserAudioSelectorControl`](../iouseraudioselectorcontrol.md) to override this class’ behavior, don’t use [`Create`](./create.md) to allocate and initialize the custom subclass.

## Parameters

- `in_driver`: The [`IOUserAudioDriver`](../iouseraudiodriver.md) that owns this object.
- `in_is_settable`: A Boolean value that indicates if the control can be set.
- `in_control_element`: An [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) to identify the control.
- `in_control_scope`: A [`IOUserAudioObjectPropertyScope`](../audiodriverkit-page/iouseraudioobjectpropertyscope.md) indicating the control’s scope: input, output, global, or play-through.
- `in_control_class_id`: The [`IOUserAudioClassID`](../audiodriverkit-page/iouseraudioclassid.md) of the control.

## See Also

### Creating a Selector Control
- [init](./init.md)
  Initializes an instance of a selector control.
- [IOUserAudioDriver](../iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [IOUserAudioObjectPropertyElement](../audiodriverkit-page/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyScope](../audiodriverkit-page/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/create)*