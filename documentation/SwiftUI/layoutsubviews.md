# LayoutSubviews

**Framework**: SwiftUI  
**Kind**: struct

A collection of proxy values that represent the subviews of a layout view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct LayoutSubviews
```

#### Overview

You receive a `LayoutSubviews` input to your implementations of [`Layout`](layout.md) protocol methods, like [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) and [`sizeThatFits(proposal:subviews:cache:)`](layout/sizethatfits(proposal:subviews:cache:).md). The `subviews` parameter (which the protocol aliases to the [`Layout.Subviews`](layout/subviews.md) type) is a collection that contains proxies for the layout’s subviews (of type [`LayoutSubview`](layoutsubview.md)). The proxies appear in the collection in the same order that they appear in the [`ViewBuilder`](viewbuilder.md) input to the layout container. Use the proxies to perform layout operations.

Access the proxies in the collection as you would the contents of any Swift random-access collection. For example, you can enumerate all of the subviews and their indices to inspect or operate on them:

```swift
for (index, subview) in subviews.enumerated() {
    // ...
}
```

## Topics

### Getting the layout direction
- [var layoutDirection: LayoutDirection](layoutsubviews/layoutdirection.md)
  The layout direction inherited by the container view.
### Accessing subviews
- [subscript(_:)](layoutsubviews/subscript(_:).md)
  Gets the subview proxies in the specified range.
- [var startIndex: Int](layoutsubviews/startindex.md)
  The index of the first subview.
- [var endIndex: Int](layoutsubviews/endindex.md)
  An index that’s one higher than the last subview.
- [LayoutSubviews.Element](layoutsubviews/element.md)
  A type that contains a proxy value.
- [LayoutSubviews.Index](layoutsubviews/index.md)
  A type that you can use to index proxy values.
- [LayoutSubviews.SubSequence](layoutsubviews/subsequence.md)
  A type that contains a subsequence of proxy values.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md)
  Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [protocol Layout](layout.md)
  A type that defines the geometry of a collection of views.
- [struct LayoutSubview](layoutsubview.md)
  A proxy that represents one subview of a layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubviews)*