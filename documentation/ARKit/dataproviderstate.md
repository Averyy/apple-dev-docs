# DataProviderState

**Framework**: ARKit  
**Kind**: enum

The possible states of a data provider.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum DataProviderState
```

## Topics

### Getting the state of a data provider
- [DataProviderState.initialized](dataproviderstate/initialized.md)
  The data provider has been created.
- [DataProviderState.running](dataproviderstate/running.md)
  The data provider is running.
- [DataProviderState.stopped](dataproviderstate/stopped.md)
  The data provider is stopped.
- [DataProviderState.paused](dataproviderstate/paused.md)
  The data provider is paused.
### Comparing data provider states
- [var description: String](dataproviderstate/description.md)
  A textual representation of the state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [protocol TrackableAnchor](trackableanchor.md)
  An anchor that can gain and lose its tracking state over the course of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/dataproviderstate)*