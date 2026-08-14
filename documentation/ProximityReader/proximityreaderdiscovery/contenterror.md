# ProximityReaderDiscovery.ContentError

**Framework**: ProximityReader  
**Kind**: enum

Errors that indicate a problem occurred when getting or showing content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

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

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery/contenterror)*