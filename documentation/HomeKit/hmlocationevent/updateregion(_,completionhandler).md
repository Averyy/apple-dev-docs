# updateRegion(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Changes the region associated with this event.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the mutable [`region`](../hmmutablelocationevent/region.md) property on the [`HMMutableLocationEvent`](../hmmutablelocationevent.md) subclass of [`HMLocationEvent`](../hmlocationevent.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func updateRegion(_ region: CLRegion, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

*Mac Catalyst*

```swift
func updateRegion(_ region: CLRegion) async throws
```

```objc
- (void) updateRegion:(CLRegion *) region completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `region`: New region on which the event is triggered. Must have at least one of [`notifyOnEntry`](../../CoreLocation/clregion/notifyonentry.md) or [`notifyOnExit`](../../CoreLocation/clregion/notifyonexit.md) set to [`true`](../../Swift/true.md).
- `completion`: The block executed when the region update request has been processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/updateregion(_:completionhandler:))*