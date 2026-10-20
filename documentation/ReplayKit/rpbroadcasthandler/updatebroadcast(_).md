# updateBroadcast(_:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Sends the current broadcast URL to the broadcast controller.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

## Declaration

```swift
func updateBroadcast(_ broadcastURL: URL)
```

```objc
- (void) updateBroadcastURL:(NSURL *) broadcastURL;
```

#### Discussion

This method updates the [`broadcastURL`](../rpbroadcastcontroller/broadcasturl.md) property for the broadcast controller.

## Parameters

- `broadcastURL`: A URL that specifies where the broadcast to be passed to the broadcasting app is contained.

## See Also

### Updating Current Broadcast Information
- [func updateServiceInfo([String : any NSCoding & NSObjectProtocol])](./updateserviceinfo%28_%29.md)
  Sends information about the current broadcast to the broadcasting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler/updatebroadcast(_:))*