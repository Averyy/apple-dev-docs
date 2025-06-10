# MKMapSnapshotter.Snapshot

**Framework**: MapKit  
**Kind**: class

An image that a snapshotter object generates.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class Snapshot
```

#### Overview

You don’t create instances of this class directly. Instead, you use an [`MKMapSnapshotter`](mkmapsnapshotter.md) object to capture the map contents asynchronously. An `MKMapSnapshotter.Snapshot` object contains the image that the snapshotter generates from the map contents.

Snapshot images don’t include any custom overlays or annotations that your app adds to the map view. If you want your annotations and overlays to appear on the final image, you need to draw them yourself. To position those items correctly on the image, use the [`point(for:)`](mkmapsnapshotter/snapshot/point(for:).md) method of this class to translate the overlay or annotation coordinate value to an appropriate location inside the image’s coordinate space.

## Topics

### Getting the snapshot image
- [var image: UIImage](mkmapsnapshotter/snapshot/image.md)
  The image of the map’s content.
- [var appearance: NSAppearance](mkmapsnapshotter/snapshot/appearance.md)
  The visual style that MapKit uses when rendering the snapshot.
### Getting points on the image
- [func point(for: CLLocationCoordinate2D) -> CGPoint](mkmapsnapshotter/snapshot/point(for:).md)
  Converts the specified map coordinate to a point in the coordinate space of the image.
### Getting appearance traits
- [var traitCollection: UITraitCollection](mkmapsnapshotter/snapshot/traitcollection.md)
  Traits to use when creating the snapshot.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKMapSnapshotter](mkmapsnapshotter.md)
  A utility class for capturing a map and its content into an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot)*