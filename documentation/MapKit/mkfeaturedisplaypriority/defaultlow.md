# defaultLow

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

A constant indicating that the item’s display priority is low.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var defaultLow: MKFeatureDisplayPriority { get }
```

```c
static const MKFeatureDisplayPriority MKFeatureDisplayPriorityDefaultLow;
```

#### Discussion

An annotation view with this priority is removed from the map when its bounds collide with the bounds of another view with a higher priority. If the priorities of the two views are equal, the view furthest from the center of the map’s visible region is hidden first.

## See Also

### Priorities
- [static var required: MKFeatureDisplayPriority](./required.md)
  A constant indicating that the item is required.
- [static var defaultHigh: MKFeatureDisplayPriority](./defaulthigh.md)
  A constant indicating that the item’s display priority is high.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkfeaturedisplaypriority/defaultlow)*