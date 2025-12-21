# viewDidUnhide()

**Framework**: AppKit  
**Kind**: method

Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func viewDidUnhide()
```

#### Discussion

The view receives this message when its `isHiddenOrHasHiddenAncestor` state goes from [`true`](https://developer.apple.com/documentation/Swift/true) to [`false`](https://developer.apple.com/documentation/Swift/false).  This can happen when the view or an ancestor is marked as not hidden, or when the view or an ancestor is removed from its containing view hierarchy.

## See Also

- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](nsview/ishiddenorhashiddenancestor.md)
  A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.
- [func viewDidHide()](nsview/viewdidhide.md)
  Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidunhide())*