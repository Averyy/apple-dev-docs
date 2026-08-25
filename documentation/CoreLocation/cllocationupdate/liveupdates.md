# liveUpdates(_:)

**Framework**: Core Location  
**Kind**: method

Tells Core Location to start delivering the location updates it produces for the configuration you specify.

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
static func liveUpdates(_ configuration: CLLocationUpdate.LiveConfiguration = .default) -> CLLocationUpdate.Updates
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Return Value

[`CLLocationUpdate.Updates`](cllocationupdate/updates.md) that meet the criteria you specify.

## Parameters

- `configuration`: A configuration that describes the updates for the framework to deliver.

## See Also

- [CLLocationUpdate.LiveConfiguration](cllocationupdate/liveconfiguration.md)
  Values that indicate the kind of positioning updates the framework delivers.
- [CLLocationUpdate.Updates](cllocationupdate/updates.md)
  A structure that represents an asynchronous sequence of location updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveupdates(_:))*