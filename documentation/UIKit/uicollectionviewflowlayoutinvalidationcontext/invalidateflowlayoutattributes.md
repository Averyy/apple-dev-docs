# invalidateFlowLayoutAttributes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether to recompute the layout attributes for items and views in the layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var invalidateFlowLayoutAttributes: Bool { get set }
```

```objc
@property (nonatomic) BOOL invalidateFlowLayoutAttributes;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). Set this property to [`true`](../../Swift/true.md) if there are changes to the position of items on the screen. For example, the flow layout object sets this property to [`true`](../../Swift/true.md) when the collection view’s bounds change in a way that affects the number of items in a column or row.

When this property is set to [`true`](../../Swift/true.md), the flow layout object recomputes the layout attributes for its items and views. If the [`invalidateFlowLayoutDelegateMetrics`](./invalidateflowlayoutdelegatemetrics.md) property is set to [`false`](../../Swift/false.md) it recomputes this information without asking for new size information.

## See Also

### Specifying what to invalidate
- [var invalidateFlowLayoutDelegateMetrics: Bool](./invalidateflowlayoutdelegatemetrics.md)
  A Boolean indicating whether to recompute the size of items and views in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes)*