# CPBarButtonHandler

**Framework**: CarPlay  
**Kind**: typealias  
**Role**: Type Alias

A block that CarPlay calls when the user taps a bar button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
typealias CPBarButtonHandler = (CPBarButton) -> Void
```

```c
typedef void (^)(CPBarButton *) CPBarButtonHandler;
```

## See Also

### Creating a bar button
- [init(image: UIImage, handler: CPBarButtonHandler?)](./cpbarbutton/init%28image,handler%29.md)
  Creates a bar button that displays an image.
- [init(title: String, handler: CPBarButtonHandler?)](./cpbarbutton/init%28title,handler%29.md)
  Creates a bar button that displays a text string.
- [init?(coder: NSCoder)](./cpbarbutton/init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonhandler)*