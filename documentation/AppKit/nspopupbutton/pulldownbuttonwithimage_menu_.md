# pullDownButtonWithImage:menu:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a standard pull-down button with an image and menu.

**Availability**:
- macOS 15.0+

## Declaration

```objc
+ (instancetype) pullDownButtonWithImage:(NSImage *) image menu:(NSMenu *) menu;
```

#### Return Value

An initialized pull-down button object.

#### Discussion

Pull-down buttons created using this method have the `usesItemFromMenu` property set to `NO`.

## Parameters

- `image`: The icon that is displayed on the button.
- `menu`: The pull-down menu to present when interacting with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/pulldownbuttonwithimage:menu:)*