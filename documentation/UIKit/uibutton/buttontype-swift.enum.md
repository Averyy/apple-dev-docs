# UIButton.ButtonType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the style of a button.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ButtonType
```

```c
enum UIButtonType : NSInteger;
```

## Topics

### Constants
- [UIButton.ButtonType.custom](./buttontype-swift.enum/custom.md)
  No button style.
- [UIButton.ButtonType.system](./buttontype-swift.enum/system.md)
  A system style button, such as those shown in navigation bars and toolbars.
- [UIButton.ButtonType.detailDisclosure](./buttontype-swift.enum/detaildisclosure.md)
  A detail disclosure button.
- [UIButton.ButtonType.infoLight](./buttontype-swift.enum/infolight.md)
  An information button that has a light background.
- [UIButton.ButtonType.infoDark](./buttontype-swift.enum/infodark.md)
  An information button that has a dark background.
- [UIButton.ButtonType.contactAdd](./buttontype-swift.enum/contactadd.md)
  A contact add button.
- [UIButton.ButtonType.plain](./buttontype-swift.enum/plain.md)
  A standard system button without a blurred background view.
- [UIButton.ButtonType.close](./buttontype-swift.enum/close.md)
  A close button to dismiss panels and views.
- [static var roundedRect: UIButton.ButtonType](./buttontype-swift.enum/roundedrect.md)
  A rounded-rectangle style button.
### Initializers
- [init?(rawValue: Int)](./buttontype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating buttons of a specific type
- [convenience init(type: UIButton.ButtonType)](./init%28type%29.md)
  Creates and returns a new button of the specified type.
- [convenience init(type: UIButton.ButtonType, primaryAction: UIAction?)](./init%28type,primaryaction%29.md)
  Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.
- [+ buttonWithType:primaryAction:](./buttonwithtype_primaryaction_.md)
  Creates a new button with the specified type, registers the primary action event, and sets the title and image to the action’s title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/buttontype-swift.enum)*