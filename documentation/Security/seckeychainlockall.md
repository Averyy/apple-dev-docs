# SecKeychainLockAll()

**Framework**: Security  
**Kind**: func

Locks all keychains belonging to the current user.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainLockAll() -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Your application should not call this function unless you are responding to a user’s request to lock a keychain. In general, you should leave the keychain unlocked so that the user does not have to unlock it again in another application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainlockall())*