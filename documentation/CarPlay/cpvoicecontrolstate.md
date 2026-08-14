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
### Initializers
- [init?(coder: NSCoder)](cpvoicecontrolstate/init(coder:).md)
- [init(identifier: String, titleVariants: [String]?, image: UIImage?, backgroundImage: UIImage?, repeats: Bool)](cpvoicecontrolstate/init(identifier:titlevariants:image:backgroundimage:repeats:).md)
  Initialize a voice control state with a title and image.
### Instance Properties
- [var actionButtons: [CPButton]](cpvoicecontrolstate/actionbuttons.md)
  An array of action buttons displayed in the template.
- [var backgroundImage: UIImage?](cpvoicecontrolstate/backgroundimage.md)
  A custom background image to be displayed behind the voice control template content.
### Type Properties
- [class var maximumActionButtonCount: Int](cpvoicecontrolstate/maximumactionbuttoncount.md)
  The maximum number of action buttons that can be displayed in the CPVoiceControlTemplate.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [init(voiceControlStates: [CPVoiceControlState])](cpvoicecontroltemplate/init(voicecontrolstates:).md)
  Creates a voice control template with a list of voice control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate)*