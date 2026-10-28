# authorize(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Attempts to unlock the lock icon in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func authorize(_ inSender: Any!) -> Bool
```

```objc
- (BOOL) authorize:(id) inSender;
```

## Discussion

This method has the same behavior as if the user clicked on the lock icon; if the user is authorized, the lock icon unlocks. If this method succeeds, it returns [`true`](../../Swift/true.md); if it fails, the lock icon remains locked and the method returns [`false`](../../Swift/false.md).

## Parameters

- `inSender`: The authorization view to unlock.

## See Also

### Related Documentation
- [func deauthorize(Any!) -> Bool](./deauthorize%28_%29.md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.
- [func authorizationState() -> SFAuthorizationViewState](./authorizationstate%28%29.md)
  Returns the current state of the authorization view.
### Setting the authorization state
- [func deauthorize(Any!) -> Bool](./deauthorize%28_%29.md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/authorize(_:))*