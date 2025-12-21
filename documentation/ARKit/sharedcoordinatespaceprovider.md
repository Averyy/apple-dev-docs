# SharedCoordinateSpaceProvider

**Framework**: ARKit  
**Kind**: class

Provides ability to establish a shared coordinate space among multiple participants.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final class SharedCoordinateSpaceProvider
```

## Topics

### Structures
- [SharedCoordinateSpaceProvider.CoordinateSpaceData](sharedcoordinatespaceprovider/coordinatespacedata.md)
  A coordinate space data.
### Initializers
- [init()](sharedcoordinatespaceprovider/init.md)
  Create a shared coordinate space provider.
### Instance Properties
- [var description: String](sharedcoordinatespaceprovider/description.md)
  A textual representation of this SharedCoordinateSpaceProvider.
- [var eventUpdates: some AsyncSequence<SharedCoordinateSpaceProvider.Event, Never>](sharedcoordinatespaceprovider/eventupdates.md)
  A sequence of events that have occurred.
- [var nextCoordinateSpaceData: SharedCoordinateSpaceProvider.CoordinateSpaceData?](sharedcoordinatespaceprovider/nextcoordinatespacedata.md)
  Get the next coordinate space data to be broadcast to all participants.
- [var participantIdentifier: UUID](sharedcoordinatespaceprovider/participantidentifier.md)
  Get the identifier of the local participant.
- [var state: DataProviderState](sharedcoordinatespaceprovider/state.md)
  The state of this shared coordinate space provider.
### Instance Methods
- [func push(data: SharedCoordinateSpaceProvider.CoordinateSpaceData)](sharedcoordinatespaceprovider/push(data:).md)
  Push data to shared coordinate space provider.
### Type Properties
- [static var isSupported: Bool](sharedcoordinatespaceprovider/issupported.md)
  Determines whether this device supports the shared coordinate space provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](sharedcoordinatespaceprovider/requiredauthorizations.md)
  The authorization type(s) required by the shared coordinate space provider.
### Enumerations
- [SharedCoordinateSpaceProvider.Event](sharedcoordinatespaceprovider/event.md)
  Events that can occur in a shared coordinate space.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/sharedcoordinatespaceprovider)*