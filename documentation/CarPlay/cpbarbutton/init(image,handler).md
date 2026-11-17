# init(image:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a bar button that displays an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(image: UIImage, handler: CPBarButtonHandler? = nil)
```

```objc
- (instancetype) initWithImage:(UIImage *) image handler:(CPBarButtonHandler) handler;
```

## Return Value

An initialized button.

## Parameters

- `image`: The image to display in the button. Provide an image that scales readily to different interface sizes. For best results, initialize your image object with an SF Symbol.
- `handler`: The code to run when someone selects the button. You might use this handler to display another template, change the sort order of list items, or perform other app-specific actions.

## See Also

### Creating a bar button
- [init(title: String, handler: CPBarButtonHandler?)](./init%28title,handler%29.md)
  Creates a bar button that displays a text string.
- [typealias CPBarButtonHandler](../cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(image:handler:))*