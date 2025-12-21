# LayoutSubview

**Framework**: SwiftUI  
**Kind**: struct

A proxy that represents one subview of a layout.

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
struct LayoutSubview
```

#### Overview

This type acts as a proxy for a view that your custom layout container places in the user interface. [`Layout`](layout.md) protocol methods receive a [`LayoutSubviews`](layoutsubviews.md) collection that contains exactly one proxy for each of the subviews arranged by your container.

Use a proxy to get information about the associated subview, like its dimensions, layout priority, or custom layout values. You also use the proxy to tell its corresponding subview where to appear by calling the proxy’s [`place(at:anchor:proposal:)`](layoutsubview/place(at:anchor:proposal:).md) method. Do this once for each subview from your implementation of the layout’s [`placeSubviews(in:proposal:subviews:cache:)`](layout/placesubviews(in:proposal:subviews:cache:).md) method.

You can read custom layout values associated with a subview by using the property’s key as an index on the subview. For more information about defining, setting, and reading custom values, see [`LayoutValueKey`](layoutvaluekey.md).

## Topics

### Placing the subview
- [func place(at: CGPoint, anchor: UnitPoint, proposal: ProposedViewSize)](layoutsubview/place(at:anchor:proposal:).md)
  Assigns a position and proposed size to the subview.
### Getting subview characteristics
- [func dimensions(in: ProposedViewSize) -> ViewDimensions](layoutsubview/dimensions(in:).md)
  Asks the subview for its dimensions and alignment guides.
- [func sizeThatFits(ProposedViewSize) -> CGSize](layoutsubview/sizethatfits(_:).md)
  Asks the subview for its size.
- [var spacing: ViewSpacing](layoutsubview/spacing.md)
  The subviews’s preferred spacing values.
- [var priority: Double](layoutsubview/priority.md)
  The layout priority of the subview.
### Getting custom values
- [subscript<K>(K.Type) -> K.Value](layoutsubview/subscript(_:).md)
  Gets the value for the subview that’s associated with the specified key.
### Instance Properties
- [var containerValues: ContainerValues](layoutsubview/containervalues.md)
  The container values associated with the given subview.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md)
  Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [protocol Layout](layout.md)
  A type that defines the geometry of a collection of views.
- [struct LayoutSubviews](layoutsubviews.md)
  A collection of proxy values that represent the subviews of a layout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubview)*