# ProximityReaderDiscovery.ContentError

**Framework**: ProximityReader  
**Kind**: enum

Errors that indicate a problem occurred when getting or showing content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum ContentError
```

## Topics

### Getting the errors
- [ProximityReaderDiscovery.ContentError.contentNotFound](proximityreaderdiscovery/contenterror/contentnotfound.md)
  An error that indicates the requested content isn’t available.
- [ProximityReaderDiscovery.ContentError.contentDisplayFailed](proximityreaderdiscovery/contenterror/contentdisplayfailed.md)
  An error that indicates an issue occurred when trying to display the requested content.
- [ProximityReaderDiscovery.ContentError.notSupported](proximityreaderdiscovery/contenterror/notsupported.md)
  An error that indicates the current device doesn’t support the requested content.
- [ProximityReaderDiscovery.ContentError.networkUnavailable](proximityreaderdiscovery/contenterror/networkunavailable.md)
  An error that indicates the system can’t reach the network.
- [ProximityReaderDiscovery.ContentError.systemBusy](proximityreaderdiscovery/contenterror/systembusy.md)
  An error that indicates the system is busy.
- [ProximityReaderDiscovery.ContentError.unknown](proximityreaderdiscovery/contenterror/unknown.md)
  An error that indicates the framework encountered a problem that the system can’t interpret.
### Operators
- [static func == (ProximityReaderDiscovery.ContentError, ProximityReaderDiscovery.ContentError) -> Bool](proximityreaderdiscovery/contenterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](proximityreaderdiscovery/contenterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](proximityreaderdiscovery/contenterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](proximityreaderdiscovery/contenterror/equatable-implementations.md)
- [Error Implementations](proximityreaderdiscovery/contenterror/error-implementations.md)
- [LocalizedError Implementations](proximityreaderdiscovery/contenterror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/contenterror)*