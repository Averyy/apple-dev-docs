# init(alignment:scope:)

**Framework**: MapKit  
**Kind**: init

Creates a scale view with the provided alignment and scope.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(alignment: HorizontalAlignment = .leading, scope: Namespace.ID? = nil)
```

#### Return Value

An initialized scale view.

## Parameters

- `alignment`: The alignment that describes the positioning of the scale view. The default is  .
- `scope`: A   value that identifies this namespace and that you can use to associate this control with a map instance.

## See Also

- [init(anchorEdge: HorizontalEdge, scope: Namespace.ID?)](mapscaleview/init(anchoredge:scope:).md)
  Creates a map scale view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapscaleview/init(alignment:scope:))*