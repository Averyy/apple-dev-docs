# session(_:didFailWithError:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when a serious error has occurred in the session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
optional func session(_ session: GKSession, didFailWithError error: any Error)
```

```objc
- (void) session:(GKSession *) session didFailWithError:(NSError *) error;
```

#### Discussion

This method is called when a serious internal error occurred in the session. Your application should disconnect the session from other peers and release the session.

## Parameters

- `session`: The session that failed.
- `error`: The error that occurred.

## See Also

### Connection Errors
- [func session(GKSession, connectionWithPeerFailed: String, withError: any Error)](./session%28_,connectionwithpeerfailed,witherror%29.md)
  Received by the delegate when an attempt to connect to another peer failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate/session(_:didfailwitherror:))*