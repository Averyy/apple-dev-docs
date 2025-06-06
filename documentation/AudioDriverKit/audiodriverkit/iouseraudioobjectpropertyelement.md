# IOUserAudioObjectPropertyElement

**Framework**: AudioDriverKit  
**Kind**: typealias

A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
typedef uint32_t IOUserAudioObjectPropertyElement;
```

#### Discussion

The element selects one of possibly many items in the section of the object in which to look for the property. Element numbers begin with the main element, `0`, and increase sequentially.

Elements are particular to an instance of a class, meaning that two instances can have different numbers of elements in the same scope. There’s no inheritance of elements.

## See Also

- [Create](iouseraudiobooleancontrol/create.md)
  Allocates and initializes an instance of the Boolean control class.
- [init](iouseraudiobooleancontrol/init.md)
  Initializes an instance of a Boolean control.
- [IOUserAudioObjectPropertyScope](audiodriverkit/iouseraudioobjectpropertyscope.md)
  A four character code which, along with the selector and element, identify a specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioobjectpropertyelement)*