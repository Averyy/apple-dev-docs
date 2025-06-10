# init(_:coordinate:anchor:accessoryAnchor:content:)

**Framework**: MapKit  
**Kind**: init

Creates an annotation that displays a view at a coordinate on the map.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, accessoryAnchor: UnitPoint, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleResource`: The localized string for the title.
- `coordinate`: The coordinate to display the annotation at.
- `anchor`: How to place the content around the provided coordinate.
- `accessoryAnchor`: How to place accessories around the provided content.
- `content`: The view to place on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:accessoryanchor:content:)-8wi4r)*