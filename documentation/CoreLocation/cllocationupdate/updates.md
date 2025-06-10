# CLLocationUpdate.Updates

**Framework**: Core Location  
**Kind**: struct

A structure that represents an asynchronous sequence of location updates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Updates
```

#### Overview

[`CLLocationUpdate`](cllocationupdate.md) uses this structure to asynchronously deliver a stream of location updates to your app when you call [`liveUpdates(_:)`](cllocationupdate/liveupdates(_:).md).

## Topics

### Type aliases
- [CLLocationUpdate.Updates.Iterator](cllocationupdate/updates/iterator.md)
  The type of the update’s iterator.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func liveUpdates(CLLocationUpdate.LiveConfiguration) -> CLLocationUpdate.Updates](cllocationupdate/liveupdates(_:).md)
  Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [CLLocationUpdate.LiveConfiguration](cllocationupdate/liveconfiguration.md)
  Values for indicating the kind of updates the framework delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate/updates)*