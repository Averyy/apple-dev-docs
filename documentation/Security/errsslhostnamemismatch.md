# errSSLHostNameMismatch

**Framework**: Security  
**Kind**: var

The host name you connected with does not match any of the host names allowed by the certificate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var errSSLHostNameMismatch: OSStatus { get }
```

#### Discussion

This is commonly caused by an incorrect value for the [`kCFStreamSSLPeerName`](https://developer.apple.com/documentation/CFNetwork/kCFStreamSSLPeerName) property within the dictionary associated with the stream’s [`kCFStreamPropertySSLSettings`](https://developer.apple.com/documentation/CFNetwork/kCFStreamPropertySSLSettings) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errsslhostnamemismatch)*