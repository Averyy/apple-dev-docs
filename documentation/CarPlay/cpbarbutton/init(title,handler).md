# init(title:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a bar button that displays a text string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(title: String, handler: CPBarButtonHandler? = nil)
```

```objc
- (instancetype) initWithTitle:(NSString *) title handler:(CPBarButtonHandler) handler;
```

## Return Value

An initialized button.

## Parameters

- `title`: The text to display in the button. CarPlay sizes the button to fit the entire string, so keep the text short. Buttons with too much text don’t leave enough room for other content in the navigation bar.
- `handler`: The code to run when someone selects the button. You might use this handler to display another template, change the sort order of list items, or perform other app-specific actions.

## See Also

### Creating a bar button
- [init(image: UIImage, handler: CPBarButtonHandler?)](./init%28image,handler%29.md)
  Creates a bar button that displays an image.
- [typealias CPBarButtonHandler](../cpbarbuttonhandler.md)
  A block that CarPlay calls when the user taps a bar button.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbutton/init(title:handler:))*