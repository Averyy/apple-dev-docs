# target

**Framework**: AppKit  
**Kind**: property

The menu item’s target.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

#### Discussion

To ensure that a menu item’s target can receive commands while a modal dialog is open, the target object should return [`true`](https://developer.apple.com/documentation/Swift/true) in [`worksWhenModal`](nspanel/workswhenmodal.md).

## See Also

- [var action: Selector?](nsmenuitem/action.md)
  The menu item’s action-method selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/target)*