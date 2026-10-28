# deauthorize(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the authorization state to unauthorized and locks the lock icon in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func deauthorize(_ inSender: Any!) -> Bool
```

```objc
- (BOOL) deauthorize:(id) inSender;
```

## Discussion

If this method succeeds, it returns [`true`](../../Swift/true.md); if it fails, the lock icon remains unlocked and the method returns [`false`](../../Swift/false.md).

## Parameters

- `inSender`: The authorization view to lock.

## See Also

### Setting the authorization state
- [func authorize(Any!) -> Bool](./authorize%28_%29.md)
  Attempts to unlock the lock icon in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/deauthorize(_:))*