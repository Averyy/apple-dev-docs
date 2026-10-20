# MKLookAroundSnapshotter.Options

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

Values you use to customize LookAround snapshots.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class Options
```

```objc
@interface MKLookAroundSnapshotOptions : NSObject
```

## Topics

### Customizing Snaphot Appearance
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./options/pointofinterestfilter.md)
  A filter to use to customize what map features are visible in the snapshot.
- [var size: CGSize](./options/size.md)
  The requested size of the snapshot image.
- [var traitCollection: UITraitCollection](./options/traitcollection.md)
  A collection of traits that describes orientation and other characteristics of the snapshot.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundsnapshotter/options)*