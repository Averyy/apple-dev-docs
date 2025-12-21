# invalidateFlowLayoutAttributes

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the flow layout object should invalidate its current attributes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var invalidateFlowLayoutAttributes: Bool { get set }
```

#### Discussion

Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) tells the flow layout object to keep its existing layout information, effectively stopping the invalidation process. Typically, you set this property to [`false`](https://developer.apple.com/documentation/Swift/false) only if you subclass [`NSCollectionViewFlowLayout`](nscollectionviewflowlayout.md) and update changed layout information directly.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which causes the flow layout object to throw out its existing layout information and recompute it.

## See Also

- [var invalidateFlowLayoutDelegateMetrics: Bool](nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics.md)
  A Boolean value indicating whether the flow layout object should fetch new size information from its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes)*