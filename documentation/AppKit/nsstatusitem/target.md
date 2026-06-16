# target

**Framework**: AppKit  
**Kind**: property

The object that receives the status item’s action message when someone clicks the status item.

**Availability**:
- macOS 10.0+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

#### Discussion

If the status item has a menu set, clicking the status item doesn’t send the action to the target; instead, the click causes the menu to appear.

## See Also

- [var action: Selector?](nsstatusitem/action.md)
  The selector the status item sends to its target when someone clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/target)*