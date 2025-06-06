# invalidateFlowLayoutDelegateMetrics

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the flow layout object should fetch new size information from its delegate.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var invalidateFlowLayoutDelegateMetrics: Bool { get set }
```

#### Discussion

As part of the invalidation process, the flow layout object normally asks its delegate to provide size information for the items in the flow layout. This behavior is necessary when the size of the items can change because it ensures that the corresponding layout attributes are always updated. However, if you know that the size of items has not changed, you can set this property to [`false`](https://developer.apple.com/documentation/swift/false). Doing so causes the flow layout to use its existing size information rather than querying the delegate, which saves time.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), which causes the flow layout object to query the delegate for new size information.

## See Also

- [var invalidateFlowLayoutAttributes: Bool](nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes.md)
  A Boolean value indicating whether the flow layout object should invalidate its current attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics)*