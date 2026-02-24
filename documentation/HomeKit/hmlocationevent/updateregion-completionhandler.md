# updateRegion(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Changes the region associated with this event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func updateRegion(_ region: CLRegion) async throws
```

## Parameters

- `region`: New region on which the event is triggered. Must have at least one of [`notifyOnEntry`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnEntry) or [`notifyOnExit`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnExit) set to [`true`](https://developer.apple.com/documentation/Swift/true).
- `completion`: The block executed when the region update request has been processed. - **error**: `nil` on success; otherwise, error object indicating the reason for failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/updateregion(_:completionhandler:))*