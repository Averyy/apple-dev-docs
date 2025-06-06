# SecCreateSharedWebCredentialPassword()

**Framework**: Security  
**Kind**: func

Returns a randomly generated password.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func SecCreateSharedWebCredentialPassword() -> CFString?
```

#### Return Value

A password in the form `xxx-xxx-xxx-xxx`, where `x` is taken from the sets `abcdefghkmnopqrstuvwxy`, `ABCDEFGHJKLMNPQRSTUVWXYZ`, and `3456789`, with at least one character from each set being present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccreatesharedwebcredentialpassword())*