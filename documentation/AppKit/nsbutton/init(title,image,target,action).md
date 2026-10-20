# init(title:image:target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a standard push button with a title and image.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(title: String, image: NSImage, target: Any?, action: Selector?)
```

```objc
+ (instancetype) buttonWithTitle:(NSString *) title image:(NSImage *) image target:(id) target action:(SEL) action;
```

## Parameters

- `title`: The localized title string to display on the button.
- `image`: The image to display in the body of the button.
- `target`: The target object that receives action messages from the button.
- `action`: The action message the button sends to the target.

## See Also

### Creating standard buttons
- [convenience init(checkboxWithTitle: String, target: Any?, action: Selector?)](./init%28checkboxwithtitle,target,action%29.md)
  Creates a standard checkbox with the title you specify.
- [convenience init(image: NSImage, target: Any?, action: Selector?)](./init%28image,target,action%29.md)
  Creates a standard push button with the image you specify.
- [convenience init(radioButtonWithTitle: String, target: Any?, action: Selector?)](./init%28radiobuttonwithtitle,target,action%29.md)
  Creates a standard radio button with the title you specify.
- [convenience init(title: String, target: Any?, action: Selector?)](./init%28title,target,action%29.md)
  Creates a standard push button with the title you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/init(title:image:target:action:))*