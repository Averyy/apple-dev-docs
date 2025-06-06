# init(type:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a bar button with a type and handler.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(type: CPBarButton.Type, handler: CPBarButtonHandler? = nil)
```

#### Return Value

A bar button of the specified type.

## Parameters

- `type`: The button type.
- `handler`: The block that CarPlay invokes when the user taps the button.

## See Also

- [init?(coder: NSCoder)](cpbarbutton/init(coder:).md)
  Creates a button initialized  from data in the specified coder object.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](cpbarbutton/init(title:handler:).md)
  Creates a bar button that displays a text label.
- [CPBarButton.Type](cpbarbutton/type.md)
  Types of bar buttons.
- [typealias CPBarButtonHandler](cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(type:handler:))*