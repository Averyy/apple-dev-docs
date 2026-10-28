# init(alignment:scope:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a scale view with the provided alignment and scope.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(alignment: HorizontalAlignment = .leading, scope: Namespace.ID? = nil)
```

## Return Value

An initialized scale view.

## Parameters

- `alignment`: The alignment that describes the positioning of the scale view. The default is [`leading`](../../SwiftUI/horizontalalignment/leading.md).
- `scope`: A [`Namespace.ID`](../../SwiftUI/namespace/id.md) value that identifies this namespace and that you can use to associate this control with a map instance.

## See Also

### Creating a map scale view
- [init(anchorEdge: HorizontalEdge, scope: Namespace.ID?)](./init%28anchoredge,scope%29.md)
  Creates a map scale view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapscaleview/init(alignment:scope:))*