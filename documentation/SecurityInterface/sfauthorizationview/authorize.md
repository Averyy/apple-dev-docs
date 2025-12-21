# authorize(_:)

**Framework**: Security Interface  
**Kind**: method

Attempts to unlock the lock icon in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func authorize(_ inSender: Any!) -> Bool
```

#### Discussion

This method has the same behavior as if the user clicked on the lock icon; if the user is authorized, the lock icon unlocks. If this method succeeds, it returns [`true`](https://developer.apple.com/documentation/Swift/true); if it fails, the lock icon remains locked and the method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `inSender`: The authorization view to unlock.

## See Also

- [func deauthorize(Any!) -> Bool](sfauthorizationview/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.
- [func deauthorize(Any!) -> Bool](sfauthorizationview/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorize(_:))*