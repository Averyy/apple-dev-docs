# SecKeychainGetUserInteractionAllowed(_:)

**Framework**: Security  
**Kind**: func

Indicates whether keychain services functions that normally display a user interaction are allowed to do so.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainGetUserInteractionAllowed(_ state: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `state`: On return, a Boolean value indicating whether user interaction is permitted. If  , user interaction is allowed, and keychain services functions that display a user interface can do so as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetuserinteractionallowed(_:))*