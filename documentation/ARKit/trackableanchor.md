# TrackableAnchor

**Framework**: ARKit  
**Kind**: protocol

An anchor that can gain and lose its tracking state over the course of a session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol TrackableAnchor : Anchor
```

## Topics

### Checking an anchor’s tracking state
- [var isTracked: Bool](trackableanchor/istracked.md)
  A Boolean value that indicates whether ARKit is tracking an anchor.

## Relationships

### Inherits From
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [DeviceAnchor](deviceanchor.md)
- [HandAnchor](handanchor.md)
- [ImageAnchor](imageanchor.md)
- [ObjectAnchor](objectanchor.md)
- [WorldAnchor](worldanchor.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [enum DataProviderState](dataproviderstate.md)
  The possible states of a data provider.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/trackableanchor)*