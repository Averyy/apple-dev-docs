# popUpButtonWithMenu:target:action:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a standard pop-up button with a menu, target, and action.

**Availability**:
- macOS 15.0+

## Declaration

```objc
+ (instancetype) popUpButtonWithMenu:(NSMenu *) menu target:(id) target action:(SEL) action;
```

## Return Value

An initialized pop-up button object.

## Discussion

If `menu` is non-empty, the pop-up button uses the first item for its initial selection.

## Parameters

- `menu`: A menu presented by the pop-up button, containing items that the user can choose between.
- `target`: The target object that receives action messages from the control.
- `action`: The action message sent by the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/popupbuttonwithmenu:target:action:)*