# remoteControlSession(_:didInvalidateWithError:)

**Framework**: CarKey  
**Kind**: method  
**Required**: Yes

Notifies your delegate object that the session become invalid for the specified reason.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
func remoteControlSession(_ session: CarKeyRemoteControlSession, didInvalidateWithError: CarKeyErrorCode)
```

#### Discussion

Use this method to detect if the system invalidated the session for any reason. The system executes this method on the dispatch queue you specified when you started the session.

## Parameters

- `session`: The session that became invalid.
- `didInvalidateWithError`: The error code that contains the reason   for the invalid session. For a list of possible values,   see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate/remotecontrolsession(_:didinvalidatewitherror:))*