# invalidateFlowLayoutDelegateMetrics

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether to recompute the size of items and views in the layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var invalidateFlowLayoutDelegateMetrics: Bool { get set }
```

```objc
@property (nonatomic) BOOL invalidateFlowLayoutDelegateMetrics;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). Set this property to [`true`](../../Swift/true.md) if you’re invalidating the layout because of changes to the size of any items.

When this property is set to [`true`](../../Swift/true.md), the flow layout object recomputes the size of its items and views, querying the delegate object as needed for that information.

## See Also

### Specifying what to invalidate
- [var invalidateFlowLayoutAttributes: Bool](./invalidateflowlayoutattributes.md)
  A Boolean indicating whether to recompute the layout attributes for items and views in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics)*