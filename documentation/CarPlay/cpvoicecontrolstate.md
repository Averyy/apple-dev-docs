# CPVoiceControlState

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A voice control state containing title variants and images for use by a voice control template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPVoiceControlState
```

```objc
@interface CPVoiceControlState : NSObject
```

## Topics

### Creating a Voice Control State
- [init(identifier: String, titleVariants: [String]?, image: UIImage?, repeats: Bool)](./cpvoicecontrolstate/init%28identifier,titlevariants,image,repeats%29.md)
  Creates a voice control state.
### Getting State Information
- [var identifier: String](./cpvoicecontrolstate/identifier.md)
  The string that your app uses to identify the voice control state.
- [var titleVariants: [String]?](./cpvoicecontrolstate/titlevariants.md)
  The array of title variants for the voice control state.
- [var image: UIImage?](./cpvoicecontrolstate/image.md)
  The image displayed while the voice control template is in this state.
- [var repeats: Bool](./cpvoicecontrolstate/repeats.md)
  A Boolean value that indicates whether the display of an animated image repeats the animation sequence indefinitely.
### Initializers
- [init?(coder: NSCoder)](./cpvoicecontrolstate/init%28coder%29.md)
- [init(identifier: String, titleVariants: [String]?, image: UIImage?, backgroundImage: UIImage?, repeats: Bool)](./cpvoicecontrolstate/init%28identifier,titlevariants,image,backgroundimage,repeats%29.md)
  Initialize a voice control state with a title and image.
### Instance Properties
- [var actionButtons: [CPButton]](./cpvoicecontrolstate/actionbuttons.md)
  An array of action buttons displayed in the template.
- [var backgroundImage: UIImage?](./cpvoicecontrolstate/backgroundimage.md)
  A custom background image to be displayed behind the voice control template content.
### Type Properties
- [class var maximumActionButtonCount: Int](./cpvoicecontrolstate/maximumactionbuttoncount.md)
  The maximum number of action buttons that can be displayed in the CPVoiceControlTemplate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Creating a Voice Control Template
- [init(voiceControlStates: [CPVoiceControlState])](./cpvoicecontroltemplate/init%28voicecontrolstates%29.md)
  Creates a voice control template with a list of voice control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate)*