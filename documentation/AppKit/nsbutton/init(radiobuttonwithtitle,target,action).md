# init(radioButtonWithTitle:target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a standard radio button with the title you specify.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(radioButtonWithTitle title: String, target: Any?, action: Selector?)
```

```objc
+ (instancetype) radioButtonWithTitle:(NSString *) title target:(id) target action:(SEL) action;
```

## Parameters

- `title`: The localized title string to display on the button.
- `target`: The target object that receives action messages from the button.
- `action`: The action message the button sends to the target.

## See Also

### Creating standard buttons
- [convenience init(checkboxWithTitle: String, target: Any?, action: Selector?)](./init%28checkboxwithtitle,target,action%29.md)
  Creates a standard checkbox with the title you specify.
- [convenience init(image: NSImage, target: Any?, action: Selector?)](./init%28image,target,action%29.md)
  Creates a standard push button with the image you specify.
- [convenience init(title: String, image: NSImage, target: Any?, action: Selector?)](./init%28title,image,target,action%29.md)
  Creates a standard push button with a title and image.
- [convenience init(title: String, target: Any?, action: Selector?)](./init%28title,target,action%29.md)
  Creates a standard push button with the title you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/init(radiobuttonwithtitle:target:action:))*