# completionHandler

**Framework**: AppKit  
**Kind**: property

A completion Block that is called when the animations in the grouping are completed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var completionHandler: (() -> Void)? { get set }
```

#### Discussion

If set to a non-`nil` value, a context’s `completionHandler` is guaranteed to be called on the main thread as soon as all animations subsequently added to the current `NSAnimationContext` grouping have completed or been cancelled.

This method drives the underlying `CATransaction`[`completionBlock()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/completionBlock()) property, although the Application Kit may assign a different, intermediary `completionBlock` to the current `CATransaction`.

The completion handler waits for all animations to which the handler applies, independent of whether they are evaluated by the Application Kit or delegated to Core Animation for evaluation in the render tree before firing.

If no animations are added before the current grouping is ended—or the completionHandler is set to a different value—the handler will be invoked immediately.

## See Also

- [class func runAnimationGroup((NSAnimationContext) -> Void, completionHandler: (() -> Void)?)](nsanimationcontext/runanimationgroup(_:completionhandler:).md)
  Allows you to specify a completion block body after the set of animation actions whose completion will trigger the completion block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext/completionhandler)*