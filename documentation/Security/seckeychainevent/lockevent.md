# SecKeychainEvent.lockEvent

**Framework**: Security  
**Kind**: case

Indicates a keychain was locked.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case lockEvent
```

#### Discussion

It is impossible to distinguish between a lock event caused by an explicit request and one caused by a keychain that locked itself because of a timeout. Therefore, the `pid` parameter in the [`SecKeychainCallbackInfo`](seckeychaincallbackinfo.md) structure does not contain useful information for this event. Note that when the login session terminates, all keychains become effectively locked; however, no `kSecLockEvent` events are generated in this case.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainevent/lockevent)*