# init(coordinate:anchor:accessoryAnchor:content:label:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates an annotation that displays a view at a coordinate on the map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, accessoryAnchor: UnitPoint, @ViewBuilder content: () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `coordinate`: The coordinate position of the annotation.
- `anchor`: A [`UnitPoint`](../../SwiftUI/unitpoint.md) value that indicates how to position the content around the provided coordinate.
- `accessoryAnchor`: A [`UnitPoint`](../../SwiftUI/unitpoint.md) value that indicates how to place accessories around the provided content.
- `content`: The view to place on the map.
- `label`: The label for the annotation, including a title, and optional subtitle.

## See Also

### Creating annotations
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](./init%28_,coordinate,anchor,accessoryanchor,content%29-6rxmn.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](./init%28_,coordinate,anchor,accessoryanchor,content%29-14m3t.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(item: MKMapItem, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](./init%28item,anchor,accessoryanchor,content%29.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](./init%28_,coordinate,anchor,content%29-2w242.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](./init%28_,coordinate,anchor,content%29-6wnoh.md)
  Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content, label: () -> Label)](./init%28coordinate,anchor,content,label%29.md)
  Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/annotation/init(coordinate:anchor:accessoryanchor:content:label:))*