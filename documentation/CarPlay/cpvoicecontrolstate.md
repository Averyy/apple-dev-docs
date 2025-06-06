# CPVoiceControlState

**Framework**: CarPlay  
**Kind**: class

A voice control state containing title variants and images for use by a voice control template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPVoiceControlState
```

## Topics

### Creating a Voice Control State
- [init(identifier: String, titleVariants: [String]?, image: UIImage?, repeats: Bool)](cpvoicecontrolstate/init(identifier:titlevariants:image:repeats:).md)
  Creates a voice control state.
### Getting State Information
- [var identifier: String](cpvoicecontrolstate/identifier.md)
  The string that your app uses to identify the voice control state.
- [var titleVariants: [String]?](cpvoicecontrolstate/titlevariants.md)
  The array of title variants for the voice control state.
- [var image: UIImage?](cpvoicecontrolstate/image.md)
  The image displayed while the voice control template is in this state.
- [var repeats: Bool](cpvoicecontrolstate/repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(voiceControlStates: [CPVoiceControlState])](cpvoicecontroltemplate/init(voicecontrolstates:).md)
  Creates a voice control template with a list of voice control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate)*