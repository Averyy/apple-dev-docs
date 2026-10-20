# pointOfInterestFilter

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The filter to use for determining the points of interest that appear in the snapshot.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use preferredConfiguration

## Declaration

```swift
@NSCopying
var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

```objc
@property (nonatomic, copy, nullable) MKPointOfInterestFilter * pointOfInterestFilter;
```

## See Also

### Configuring the map data
- [var preferredConfiguration: MKMapConfiguration](./preferredconfiguration.md)
  The map configuration style to use for snapshots.
- [var mapType: MKMapType](./maptype.md)
  The map’s visual style.
- [var showsBuildings: Bool](./showsbuildings.md)
  A Boolean that indicates whether the map displays extruded building information.
- [var showsPointsOfInterest: Bool](./showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/pointofinterestfilter)*