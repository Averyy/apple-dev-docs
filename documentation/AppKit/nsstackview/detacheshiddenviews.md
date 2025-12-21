# detachesHiddenViews

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the stack view removes hidden views from its view hierarchy.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var detachesHiddenViews: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), setting the [`isHidden`](nsview/ishidden.md) property of a view to [`true`](https://developer.apple.com/documentation/Swift/true) causes the stack view to remove hidden views from its view hierarchy and put them in the [`detachedViews`](nsstackview/detachedviews.md) property. Changing the view’s [`isHidden`](nsview/ishidden.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) causes the stack view to add the view back to the view hierarchy. When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), views remain in the view hierarchy, even when they are hidden. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func setClippingResistancePriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/setclippingresistancepriority(_:for:).md)
  Sets the Auto Layout priority for resisting clipping of views in the stack view when Auto Layout attempts to reduce the stack view’s size.
- [func setHuggingPriority(NSLayoutConstraint.Priority, for: NSLayoutConstraint.Orientation)](nsstackview/sethuggingpriority(_:for:).md)
  Sets the Auto Layout priority for the stack view to minimize its size, for a specified user interface axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/detacheshiddenviews)*