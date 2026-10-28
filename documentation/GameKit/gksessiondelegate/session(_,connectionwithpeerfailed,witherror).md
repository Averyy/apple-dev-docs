# session(_:connectionWithPeerFailed:withError:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Received by the delegate when an attempt to connect to another peer failed.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: any Error)
```

```objc
- (void) session:(GKSession *) session connectionWithPeerFailed:(NSString *) peerID withError:(NSError *) error;
```

## Discussion

The `error` parameter can be used to inform the user of why the connection failed.

> ❗ **Important**:  If a [`GKPeerPickerController`](../gkpeerpickercontroller.md) object is being used to configure the session, the controller handles this message automatically. Your delegate can ignore it if the peer picker dialog is in use.

## Parameters

- `session`: The session that received the message.
- `peerID`: A string that uniquely identifies the peer.
- `error`: The error that occurred.

## See Also

### Connection Errors
- [func session(GKSession, didFailWithError: any Error)](./session%28_,didfailwitherror%29.md)
  Sent to the delegate when a serious error has occurred in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate/session(_:connectionwithpeerfailed:witherror:))*