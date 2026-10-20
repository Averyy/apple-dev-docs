# init(type:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a bar button with a type and handler.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
init(type: CPBarButton.Type, handler: CPBarButtonHandler? = nil)
```

```objc
- (instancetype) initWithType:(CPBarButtonType) type handler:(CPBarButtonHandler) handler;
```

#### Return Value

A bar button of the specified type.

## Parameters

- `type`: The button type.
- `handler`: The block that CarPlay invokes when the user taps the button.

## See Also

### Creating a CarPlay Bar Button
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a button initialized  from data in the specified coder object.
- [init(image: UIImage, handler: CPBarButtonHandler?)](./init%28image,handler%29.md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](./init%28title,handler%29.md)
  Creates a bar button that displays a text label.
- [CPBarButton.Type](./type.md)
  Types of bar buttons.
- [typealias CPBarButtonHandler](../cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(type:handler:))*