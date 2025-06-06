# updateBroadcast(_:)

**Framework**: ReplayKit  
**Kind**: method

Sends the current broadcast URL to the broadcast controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func updateBroadcast(_ broadcastURL: URL)
```

#### Discussion

This method updates the [`broadcastURL`](rpbroadcastcontroller/broadcasturl.md) property for the broadcast controller.

## Parameters

- `broadcastURL`: A URL that specifies where the broadcast to be passed to the broadcasting app is contained.

## See Also

- [func updateServiceInfo([String : any NSCoding & NSObjectProtocol])](rpbroadcasthandler/updateserviceinfo(_:).md)
  Sends information about the current broadcast to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/updatebroadcast(_:))*