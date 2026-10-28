# viewDidUnhide()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden

**Availability**:
- macOS 10.5+

## Declaration

```swift
func viewDidUnhide()
```

```objc
- (void) viewDidUnhide;
```

## Discussion

The view receives this message when its `isHiddenOrHasHiddenAncestor` state goes from [`true`](../../Swift/true.md) to [`false`](../../Swift/false.md).  This can happen when the view or an ancestor is marked as not hidden, or when the view or an ancestor is removed from its containing view hierarchy.

## See Also

### Showing and Hiding the View
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](./ishiddenorhashiddenancestor.md)
  A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.
- [func viewDidHide()](./viewdidhide%28%29.md)
  Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidunhide())*