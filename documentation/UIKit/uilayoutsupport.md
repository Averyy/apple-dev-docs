# UILayoutSupport

**Framework**: UIKit  
**Kind**: protocol

A set of methods that provide layout support and access to layout anchors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UILayoutSupport : NSObjectProtocol
```

#### Overview

This protocol is implemented by the [`UIViewController`](uiviewcontroller.md) properties [`topLayoutGuide`](uiviewcontroller/toplayoutguide.md) and [`bottomLayoutGuide`](uiviewcontroller/bottomlayoutguide.md) to support using Auto Layout with a view controller’s view. You can use layout guides as layout items in the [`NSLayoutConstraint`](nslayoutconstraint.md) factory methods.

## Topics

### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](uilayoutsupport/bottomanchor.md)
  A layout anchor representing the guide’s bottom edge.
- [var heightAnchor: NSLayoutDimension](uilayoutsupport/heightanchor.md)
  A layout anchor representing the guide’s height.
- [var topAnchor: NSLayoutYAxisAnchor](uilayoutsupport/topanchor.md)
  A layout anchor representing the guide’s top edge.
### Performing layout calculations
- [var length: CGFloat](uilayoutsupport/length.md)
  Provides the length, in points, of the portion of a view controller’s view that is overlaid by translucent or transparent UIKit bars.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [class NSLayoutConstraint](nslayoutconstraint.md)
  The relationship between two user interface objects that must be satisfied by the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutsupport)*