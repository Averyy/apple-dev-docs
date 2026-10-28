# IOUserAudioObjectPropertyElementMain

**Framework**: AudioDriverKit  
**Kind**: var  
**Role**: Global Variable

The identifier for an audio object’s main element.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
constexpr const IOUserAudioObjectPropertyElement IOUserAudioObjectPropertyElementMain;
```

## Discussion

The main element has the value `0`.

## See Also

### Working with Control Properties
- [GetControlScope](../iouseraudiocontrol/getcontrolscope.md)
  Returns the control’s scope: input, output, global, or play-through.
- [IOUserAudioObjectPropertyScope](./iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.
- [GetControlElement](../iouseraudiocontrol/getcontrolelement.md)
  Returns the control’s identifying element.
- [IOUserAudioObjectPropertyElement](./iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.
- [GetIsSettable](../iouseraudiocontrol/getissettable.md)
  Returns a Boolean value that idicates if the control can be set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioobjectpropertyelementmain)*