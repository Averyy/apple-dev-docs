# pullDownButtonWithTitle:menu:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a standard pull-down button with a title and menu.

**Availability**:
- macOS 15.0+

## Declaration

```objc
+ (instancetype) pullDownButtonWithTitle:(NSString *) title menu:(NSMenu *) menu;
```

#### Return Value

An initialized pull-down button object.

#### Discussion

Pull-down buttons created using this method have the `usesItemFromMenu` property set to `NO`.

## Parameters

- `title`: The localized title string that is displayed on the button.
- `menu`: The pull-down menu to present when interacting with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/pulldownbuttonwithtitle:menu:)*