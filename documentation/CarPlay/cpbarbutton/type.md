# CPBarButton.Type

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Types of bar buttons.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum `Type`
```

```c
enum CPBarButtonType : NSUInteger;
```

## Topics

### Button Types
- [CPBarButton.Type.text](./type/text.md)
  A text style bar button.
- [CPBarButton.Type.image](./type/image.md)
  An image style bar button.
### Initializers
- [init?(rawValue: UInt)](./type/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a CarPlay Bar Button
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a button initialized  from data in the specified coder object.
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](./init%28type,handler%29.md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](./init%28image,handler%29.md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](./init%28title,handler%29.md)
  Creates a bar button that displays a text label.
- [typealias CPBarButtonHandler](../cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/type)*