# CPBarButtonHandler

**Framework**: CarPlay  
**Kind**: typealias

A block that CarPlay calls when the user taps a bar button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
typealias CPBarButtonHandler = (CPBarButton) -> Void
```

## See Also

- [init?(coder: NSCoder)](cpbarbutton/init(coder:).md)
  Creates a button initialized  from data in the specified coder object.
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](cpbarbutton/init(type:handler:).md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](cpbarbutton/init(title:handler:).md)
  Creates a bar button that displays a text label.
- [CPBarButton.Type](cpbarbutton/type.md)
  Types of bar buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonhandler)*