# init(image:menu:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a combo button that displays an image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
convenience init(image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)
```

#### Return Value

A combo button configured with only the specified image.

#### Discussion

This method sets the [`title`](nscombobutton/title.md) property to an empty string.

## Parameters

- `image`: The image to display in the button.
- `menu`: The menu to display when someone chooses an alternate action.
- `target`: The object that receives the default action message when someone clicks the button.
- `action`: The action message to send to the   object.

## See Also

- [convenience init(title: String, image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(title:image:menu:target:action:).md)
  Creates a combo button that displays both a title and image.
- [convenience init(title: String, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(title:menu:target:action:).md)
  Creates a combo button that displays a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/init(image:menu:target:action:))*