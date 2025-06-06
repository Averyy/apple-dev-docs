# init(_:coordinate:anchor:content:)

**Framework**: MapKit  
**Kind**: init

Creates an annotation that displays a view at a coordinate on the map.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleKey: LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleKey`: The localized string key to use to look up the title.
- `coordinate`: The coordinate position of the annotation.
- `anchor`: A   value that indicates how to position the content around the provided coordinate.
- `content`: The view to place on the map.

## See Also

- [init(LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:accessoryanchor:content:)-6rxmn.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:accessoryanchor:content:)-14m3t.md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content, label: () -> Label)](annotation/init(coordinate:anchor:accessoryanchor:content:label:).md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init(item: MKMapItem, anchor: UnitPoint, accessoryAnchor: UnitPoint, content: () -> Content)](annotation/init(item:anchor:accessoryanchor:content:).md)
  Creates an annotation that displays a view at a coordinate on the map.
- [init<S>(S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content)](annotation/init(_:coordinate:anchor:content:)-6wnoh.md)
  Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate: CLLocationCoordinate2D, anchor: UnitPoint, content: () -> Content, label: () -> Label)](annotation/init(coordinate:anchor:content:label:).md)
  Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-2w242)*