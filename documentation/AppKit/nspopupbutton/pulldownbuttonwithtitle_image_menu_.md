# pullDownButtonWithTitle:image:menu:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a standard pull-down button with a title, image, and menu.

**Availability**:
- macOS 15.0+

## Declaration

```objc
+ (instancetype) pullDownButtonWithTitle:(NSString *) title image:(NSImage *) image menu:(NSMenu *) menu;
```

#### Return Value

An initialized pull-down button object.

#### Discussion

Pull-down buttons created using this method have the `usesItemFromMenu` property set to `NO`.

## Parameters

- `title`: The localized title string that is displayed on the button.
- `image`: The icon that is displayed on the button.
- `menu`: The pull-down menu to present when interacting with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/pulldownbuttonwithtitle:image:menu:)*