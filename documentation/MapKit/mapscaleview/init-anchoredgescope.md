# init(anchorEdge:scope:)

**Framework**: MapKit  
**Kind**: init

Creates a map scale view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(anchorEdge: HorizontalEdge = .leading, scope: Namespace.ID? = nil)
```

## Parameters

- `anchorEdge`: The fixed edge the scale grows and shrinks from. Use this outside of   view modifier.
- `scope`: A   value that identifies this namespace and that you can use to associate this control with a map instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapscaleview/init(anchoredge:scope:))*