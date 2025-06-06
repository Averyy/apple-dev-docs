# MKOverlayLevel

**Framework**: MapKit  
**Kind**: enum

Constants that indicate the position of overlays relative to other content.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum MKOverlayLevel
```

## Topics

### Constants
- [MKOverlayLevel.aboveRoads](mkoverlaylevel/aboveroads.md)
  Place the overlay above roadways but below map labels, shields, or point-of-interest icons.
- [MKOverlayLevel.aboveLabels](mkoverlaylevel/abovelabels.md)
  Place the overlay above map labels, shields, or point-of-interest icons but below annotations and 3D projections of buildings.
### Initializers
- [init?(rawValue: Int)](mkoverlaylevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var overlays: [any MKOverlay]](mkmapview/overlays.md)
  The overlay objects associated with the map view.
- [func overlays(in: MKOverlayLevel) -> [any MKOverlay]](mkmapview/overlays(in:).md)
  Returns overlay objects in the specified level of the map.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](mkmapview/renderer(for:).md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaylevel)*