# target

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item’s target.

**Availability**:
- macOS

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (weak, nullable) id target;
```

## Discussion

To ensure that a menu item’s target can receive commands while a modal dialog is open, the target object should return [`true`](../../Swift/true.md) in [`worksWhenModal`](../nspanel/workswhenmodal.md).

## See Also

### Managing the target and action
- [var action: Selector?](./action.md)
  The menu item’s action-method selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/target)*