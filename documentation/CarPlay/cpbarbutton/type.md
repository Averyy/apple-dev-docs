# CPBarButton.Type

**Framework**: CarPlay  
**Kind**: enum

Types of bar buttons.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum `Type`
```

## Topics

### Button Types
- [CPBarButton.Type.text](cpbarbutton/type/text.md)
  A text style bar button.
- [CPBarButton.Type.image](cpbarbutton/type/image.md)
  An image style bar button.
### Initializers
- [init?(rawValue: UInt)](cpbarbutton/type/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init?(coder: NSCoder)](cpbarbutton/init(coder:).md)
  Creates a button initialized  from data in the specified coder object.
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](cpbarbutton/init(type:handler:).md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](cpbarbutton/init(title:handler:).md)
  Creates a bar button that displays a text label.
- [typealias CPBarButtonHandler](cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/type)*