# init(popUpMenu:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a standard pop-up button with a menu, target, and action.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@backDeployed(before: macOS 15.0)
@MainActor @preconcurrency convenience init(popUpMenu: NSMenu, target: AnyObject?, action: Selector?)
```

#### Return Value

An initialized pop-up button object.

#### Discussion

If `menu` is non-empty, the pop-up button uses the first item for its initial selection.

## Parameters

- `popUpMenu`: A menu presented by the pop-up button, containing items that the user can choose between.
- `target`: The target object that receives action messages from the control.
- `action`: The action message sent by the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/init(popupmenu:target:action:))*