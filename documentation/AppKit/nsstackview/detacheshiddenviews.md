# detachesHiddenViews

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the stack view removes hidden views from its view hierarchy.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var detachesHiddenViews: Bool { get set }
```

```objc
@property BOOL detachesHiddenViews;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), setting the [`isHidden`](../nsview/ishidden.md) property of a view to [`true`](../../Swift/true.md) causes the stack view to remove hidden views from its view hierarchy and put them in the [`detachedViews`](./detachedviews.md) property. Changing the view’s [`isHidden`](../nsview/ishidden.md) property to [`false`](../../Swift/false.md) causes the stack view to add the view back to the view hierarchy. When the value of this property is [`false`](../../Swift/false.md), views remain in the view hierarchy, even when they are hidden. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring Dynamic Behavior for a Stack View
- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./setclippingresistancepriority%28_,for%29.md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](./sethuggingpriority%28_,for%29.md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/detacheshiddenviews)*