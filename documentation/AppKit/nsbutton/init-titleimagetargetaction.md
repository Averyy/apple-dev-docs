# init(title:image:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a standard push button with a title and image.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(title: String, image: NSImage, target: Any?, action: Selector?)
```

## Parameters

- `title`: The localized title string to display on the button.
- `image`: The image to display in the body of the button.
- `target`: The target object that receives action messages from the button.
- `action`: The action message the button sends to the target.

## See Also

- [convenience init(checkboxWithTitle: String, target: Any?, action: Selector?)](nsbutton/init(checkboxwithtitle:target:action:).md)
  Creates a standard checkbox with the title you specify.
- [convenience init(image: NSImage, target: Any?, action: Selector?)](nsbutton/init(image:target:action:).md)
  Creates a standard push button with the image you specify.
- [convenience init(radioButtonWithTitle: String, target: Any?, action: Selector?)](nsbutton/init(radiobuttonwithtitle:target:action:).md)
  Creates a standard radio button with the title you specify.
- [convenience init(title: String, target: Any?, action: Selector?)](nsbutton/init(title:target:action:).md)
  Creates a standard push button with the title you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/init(title:image:target:action:))*