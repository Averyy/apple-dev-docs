# GetControlScope

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the control’s scope: input, output, global, or play-through.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioObjectPropertyScope GetControlScope();
```

## Return Value

The control’s scope.

## See Also

### Working with Control Properties
- [IOUserAudioObjectPropertyScope](../audiodriverkit-page/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [GetControlElement](./getcontrolelement.md)
  Returns the control’s identifying element.
- [IOUserAudioObjectPropertyElement](../audiodriverkit-page/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [IOUserAudioObjectPropertyElementMain](../audiodriverkit-page/iouseraudioobjectpropertyelementmain.md)
  The identifier for an audio object’s main element.
- [GetIsSettable](./getissettable.md)
  Returns a Boolean value that idicates if the control can be set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocontrol/getcontrolscope)*