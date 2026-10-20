# isPaused

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the broadcast is paused.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
var isPaused: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPaused) BOOL paused;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the broadcast is paused.

## See Also

### Retrieving Information About the Broadcast
- [var broadcastExtensionBundleID: String?](./broadcastextensionbundleid.md)
  The bundle ID for the selected broadcast service.
- [var isBroadcasting: Bool](./isbroadcasting.md)
  A Boolean value indicating whether the controller is broadcasting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/ispaused)*