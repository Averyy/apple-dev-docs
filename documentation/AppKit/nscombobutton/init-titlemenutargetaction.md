# init(title:menu:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a combo button that displays a title.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
convenience init(title: String, menu: NSMenu?, target: Any?, action: Selector?)
```

#### Return Value

A combo button configured with only a title string.

#### Discussion

This method sets the [`image`](nscombobutton/image.md) property to `nil`.

## Parameters

- `title`: The localized string to display in the button. Use the inherited   property to set the text alignment for the string.
- `menu`: The menu to display when someone chooses an alternate action.
- `target`: The object that receives the default action message when someone clicks the button.
- `action`: The action message to send to the   object.

## See Also

- [convenience init(title: String, image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(title:image:menu:target:action:).md)
  Creates a combo button that displays both a title and image.
- [convenience init(image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(image:menu:target:action:).md)
  Creates a combo button that displays an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/init(title:menu:target:action:))*