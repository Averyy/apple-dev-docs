# viewDidHide()

**Framework**: AppKit  
**Kind**: method

Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func viewDidHide()
```

#### Discussion

The view receives this message when its [`isHiddenOrHasHiddenAncestor`](nsview/ishiddenorhashiddenancestor.md) property changes from [`false`](https://developer.apple.com/documentation/Swift/false) to [`true`](https://developer.apple.com/documentation/Swift/true). This happens when the view or an ancestor is marked as hidden, or when the view or an ancestor is inserted into a new view hierarchy.

## See Also

- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](nsview/ishiddenorhashiddenancestor.md)
  A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.
- [func viewDidUnhide()](nsview/viewdidunhide.md)
  Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidhide())*