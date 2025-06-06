# init(title:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a bar button that displays a text label.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(title: String, handler: CPBarButtonHandler? = nil)
```

#### Return Value

A bar button that displays the provided text.

## Parameters

- `title`: The text to display on the button.
- `handler`: The block that CarPlay invokes when the user taps the button.

## See Also

- [init?(coder: NSCoder)](cpbarbutton/init(coder:).md)
  Creates a button initialized  from data in the specified coder object.
- [init(type: CPBarButton.Type, handler: CPBarButtonHandler?)](cpbarbutton/init(type:handler:).md)
  Creates a bar button with a type and handler.
- [init(image: UIImage, handler: CPBarButtonHandler?)](cpbarbutton/init(image:handler:).md)
  Creates a bar button that displays an image.
- [CPBarButton.Type](cpbarbutton/type.md)
  Types of bar buttons.
- [typealias CPBarButtonHandler](cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(title:handler:))*