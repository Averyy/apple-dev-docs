# errSSLDecryptionFail

**Framework**: Security  
**Kind**: var

Decryption failed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var errSSLDecryptionFail: OSStatus { get }
```

#### Discussion

Among other causes, this may be caused by invalid data coming from the remote host, a damaged crypto key, or insufficient permission to use a key that is stored in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errssldecryptionfail)*