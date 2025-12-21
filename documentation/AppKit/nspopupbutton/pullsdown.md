# pullsDown

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the button displays a pull-down or pop-up menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var pullsDown: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button displays a pull-down menu; otherwise, it displays a pop-up menu. This property does not affect the contents of the menu; it affects only the style of the menu.

When changing the menu type to a pull-down menu, if the menu was a pop-up menu and the cell alters the state of its selected items, this method sets the state of the currently selected item to `NSStateOff` before changing the menu type.

## See Also

- [init(frame: NSRect, pullsDown: Bool)](nspopupbutton/init(frame:pullsdown:).md)
  Returns an `NSPopUpButton` object initialized to the specified dimensions.
- [var autoenablesItems: Bool](nspopupbutton/autoenablesitems.md)
  A Boolean value indicating whether the button enables and disables its items every time a user event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown)*