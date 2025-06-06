# IOUserAudioObjectPropertyScope

**Framework**: AudioDriverKit  
**Kind**: enum

A four character code which, along with the selector and element, identify a specific piece of information about an audio object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioObjectPropertyScope : uint32_t;
```

#### Discussion

The scope specifies the section of the object in which to look for the property, such as input, output, global, or pass-through. Each class has a different set of scopes. A subclass inherits its superclass’s set of scopes.

## Topics

### Property Scopes
- [Global](audiodriverkit/iouseraudioobjectpropertyscope/global.md)
  The scope for properties that apply to the object as a whole.
- [Input](audiodriverkit/iouseraudioobjectpropertyscope/input.md)
  The scope for properties that apply to the input side of an object.
- [Output](audiodriverkit/iouseraudioobjectpropertyscope/output.md)
  The scope for properties that apply to the output side of an object.
- [PlayThrough](audiodriverkit/iouseraudioobjectpropertyscope/playthrough.md)
  The scope for properties that apply to the play-through side of an object.

## See Also

- [Create](iouseraudiobooleancontrol/create.md)
  Allocates and initializes an instance of the Boolean control class.
- [init](iouseraudiobooleancontrol/init.md)
  Initializes an instance of a Boolean control.
- [IOUserAudioObjectPropertyElement](audiodriverkit/iouseraudioobjectpropertyelement.md)
  A four character code which, along with the selector and scope, identify a specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioobjectpropertyscope)*