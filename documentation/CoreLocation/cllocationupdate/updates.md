# CLLocationUpdate.Updates

**Framework**: Core Location  
**Kind**: struct  
**Role**: Structure

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

[`CLLocationUpdate`](../cllocationupdate.md) uses this structure to asynchronously deliver a stream of location updates to your app when you call [`liveUpdates(_:)`](./liveupdates%28_%29.md).

## Topics

### Type aliases
- [CLLocationUpdate.Updates.Iterator](./updates/iterator.md)
  The type of the update’s iterator.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving location updates
- [static func liveUpdates(CLLocationUpdate.LiveConfiguration) -> CLLocationUpdate.Updates](./liveupdates%28_%29.md)
  Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [CLLocationUpdate.LiveConfiguration](./liveconfiguration.md)
  Values that indicate the kind of positioning updates the framework delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate/updates)*