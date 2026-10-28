# MKMapSnapshotter.Options

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

The options the snapshotter initializer uses to create a snapshotter to capture map-based imagery.

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
class Options
```

```objc
@interface MKMapSnapshotOptions : NSObject
```

## Overview

After creating and configuring an instance of this class, you pass that instance to an [`MKMapSnapshotter`](../mkmapsnapshotter.md) object. The snapshotter uses the configuration options to determine which portion of the map to capture, the viewing angle to use for the camera, and the map’s overall appearance.

In macOS 10.14 and later, you can apply a light or dark appearance to your map snapshots by modifying the [`appearance`](./options/appearance.md) property of your snapshot options. Even if you specify a custom appearance, users can use the Maps app to force all maps to adopt a light appearance.

## Topics

### Configuring the snapshot region
- [var region: MKCoordinateRegion](./options/region.md)
  The area of the map that you want to capture.
- [var mapRect: MKMapRect](./options/maprect.md)
  The map rectangle that you want to capture.
- [var camera: MKMapCamera](./options/camera.md)
  The camera to use when taking the map snapshot.
### Configuring the map data
- [var preferredConfiguration: MKMapConfiguration](./options/preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var mapType: MKMapType](./options/maptype.md)
  The map’s visual style.
- [var showsBuildings: Bool](./options/showsbuildings.md)
  A Boolean that indicates whether the map displays extruded building information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./options/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear in the snapshot.
- [var showsPointsOfInterest: Bool](./options/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
### Configuring the image output
- [var traitCollection: UITraitCollection](./options/traitcollection.md)
  Traits that determine the appearance of the map snapshot.
- [var size: CGSize](./options/size.md)
  The size of the image that you want to create.
- [var appearance: NSAppearance?](./options/appearance.md)
  The visual style (light or dark) to apply to the map when rendering the snapshot image.
- [var scale: CGFloat](./options/scale.md)
  The scale factor to use when creating the image.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a snapshotter object
- [init(options: MKMapSnapshotter.Options)](./init%28options%29.md)
  Creates and returns a snapshotter object based on the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options)*