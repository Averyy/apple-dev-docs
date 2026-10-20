# isHiddenOrHasHiddenAncestor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view is hidden from sight because it, or one of its ancestors, is marked as hidden.

**Availability**:
- macOS

## Declaration

```swift
var isHiddenOrHasHiddenAncestor: Bool { get }
```

```objc
@property (readonly, getter=isHiddenOrHasHiddenAncestor) BOOL hiddenOrHasHiddenAncestor;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the value of the [`isHidden`](./ishidden.md) property is [`true`](../../Swift/true.md) for the current view or any of its ancestors in the view hierarchy. This property does not account for other reasons why a view might be considered hidden, such as being positioned outside its superview’s bounds, not having a window, or residing in a window that is offscreen or overlapped by another window.

## See Also

### Showing and Hiding the View
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [func viewDidHide()](./viewdidhide%28%29.md)
  Invoked when the view is hidden, either directly, or in response to an ancestor being hidden.
- [func viewDidUnhide()](./viewdidunhide%28%29.md)
  Invoked when the view is unhidden, either directly, or in response to an ancestor being unhidden


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/ishiddenorhashiddenancestor)*