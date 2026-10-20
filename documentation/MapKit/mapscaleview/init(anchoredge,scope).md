# init(anchorEdge:scope:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a map scale view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency init(anchorEdge: HorizontalEdge = .leading, scope: Namespace.ID? = nil)
```

## Parameters

- `anchorEdge`: The fixed edge the scale grows and shrinks from. Use this outside of [`mapControls(_:)`](../../SwiftUI/view/mapcontrols%28_%29.md) view modifier.
- `scope`: A [`Namespace.ID`](../../SwiftUI/namespace/id.md) value that identifies this namespace and that you can use to associate this control with a map instance.

## See Also

### Creating a map scale view
- [init(alignment: HorizontalAlignment, scope: Namespace.ID?)](./init%28alignment,scope%29.md)
  Creates a scale view with the provided alignment and scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapscaleview/init(anchoredge:scope:))*