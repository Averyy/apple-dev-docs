# invalidateFlowLayoutAttributes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the flow layout object should invalidate its current attributes.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var invalidateFlowLayoutAttributes: Bool { get set }
```

```objc
@property BOOL invalidateFlowLayoutAttributes;
```

#### Discussion

Setting this property to [`false`](../../Swift/false.md) tells the flow layout object to keep its existing layout information, effectively stopping the invalidation process. Typically, you set this property to [`false`](../../Swift/false.md) only if you subclass [`NSCollectionViewFlowLayout`](../nscollectionviewflowlayout.md) and update changed layout information directly.

The default value of this property is [`true`](../../Swift/true.md), which causes the flow layout object to throw out its existing layout information and recompute it.

## See Also

### Invalidating the Flow Layout
- [var invalidateFlowLayoutDelegateMetrics: Bool](./invalidateflowlayoutdelegatemetrics.md)
  A Boolean value indicating whether the flow layout object should fetch new size information from its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes)*