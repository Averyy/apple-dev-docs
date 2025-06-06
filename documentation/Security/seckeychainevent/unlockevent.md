# SecKeychainEvent.unlockEvent

**Framework**: Security  
**Kind**: case

Indicates a keychain was successfully unlocked.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case unlockEvent
```

#### Discussion

It is impossible to distinguish between an unlock event caused by an explicit request and one that occurred automatically because the keychain was needed to perform an operation. In either case, however, the `pid` parameter in the `SecKeychainCallbackInfo` structure does return the ID of the process whose actions caused the unlock event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainevent/unlockevent)*