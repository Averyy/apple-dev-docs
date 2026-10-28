# init(title:image:menu:target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a combo button that displays both a title and image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init(title: String, image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)
```

```objc
+ (instancetype) comboButtonWithTitle:(NSString *) title image:(NSImage *) image menu:(NSMenu *) menu target:(id) target action:(SEL) action;
```

## Return Value

A combo button configured with both a title and image.

## Parameters

- `title`: The localized string to display in the button. Use the inherited [`alignment`](../nscontrol/alignment.md) property to set the text alignment for the string.
- `image`: The image to display in the button.
- `menu`: The menu to display when someone chooses an alternate action.
- `target`: The object that receives the default action message when someone clicks the button.
- `action`: The action message to send to the `target` object.

## See Also

### Creating a Combo Button
- [convenience init(title: String, menu: NSMenu?, target: Any?, action: Selector?)](./init%28title,menu,target,action%29.md)
  Creates a combo button that displays a title.
- [convenience init(image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](./init%28image,menu,target,action%29.md)
  Creates a combo button that displays an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton/init(title:image:menu:target:action:))*