# deauthorize(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the authorization state to unauthorized and locks the lock icon in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func deauthorize(_ inSender: Any!) -> Bool
```

#### Discussion

If this method succeeds, it returns [`true`](https://developer.apple.com/documentation/Swift/true); if it fails, the lock icon remains unlocked and the method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `inSender`: The authorization view to lock.

## See Also

- [func authorize(Any!) -> Bool](sfauthorizationview/authorize(_:).md)
  Attempts to unlock the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/deauthorize(_:))*