# viewDidHide()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func viewDidHide()
```

```objc
- (void) viewDidHide;
```

## Discussion

The view receives this message when its [`isHiddenOrHasHiddenAncestor`](./ishiddenorhashiddenancestor.md) property changes from [`false`](../../Swift/false.md) to [`true`](../../Swift/true.md). This happens when the view or an ancestor is marked as hidden, or when the view or an ancestor is inserted into a new view hierarchy.

## See Also

### Showing and Hiding the View
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var isHiddenOrHasHiddenAncestor: Bool](./ishiddenorhashiddenancestor.md)
  A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.
- [func viewDidUnhide()](./viewdidunhide%28%29.md)
  Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewdidhide())*