# init(coder:)

**Framework**: CarPlay  
**Kind**: init

Creates a button initialized  from data in the specified coder object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init?(coder: NSCoder)
```

#### Return Value

A new button.

## See Also

- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](cpbarbutton/init(type:handler:).md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](cpbarbutton/init(title:handler:).md)
  Creates a bar button that displays a text label.
- [CPBarButton.Type](cpbarbutton/type.md)
  Types of bar buttons.
- [typealias CPBarButtonHandler](cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(coder:))*