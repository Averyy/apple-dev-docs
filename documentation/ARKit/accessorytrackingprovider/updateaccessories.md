# updateAccessories(_:)

**Framework**: ARKit  
**Kind**: method

Updates the accessories being tracked by a provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func updateAccessories(_ accessories: [Accessory]) async throws
```

#### Discussion

Updates are atomic: if any accessory fails to be added, the entire request fails and the provider continues tracking the original set of accessories.

Update requests are processed sequentially. If multiple requests are made while an update is in progress, only the most recent request is retained and will be processed next; intermediate requests are superseded and throw an error.

> **Note**: `AccessoryTrackingProvider.Error` if the update fails, including when one or more accessories cannot be added or the request is superseded by a more recent request.

## Parameters

- `accessories`: The new set of accessories to track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/updateaccessories(_:))*