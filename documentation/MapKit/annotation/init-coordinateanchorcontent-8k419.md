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
@preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text
```

#### Discussion

Uses `.center` for `accessoryAnchor`. For greater control of selection accessory positioning, please use an initializer with an `accessoryAnchor` parameter.

## Parameters

- `titleResource`: The localized string for the title.
- `coordinate`: The coordinate to display the annotation at.
- `anchor`: How to place the content around the provided coordinate.
- `content`: The view to place on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-8k419)*