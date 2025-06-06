# SecTrustResultType.deny

**Framework**: Security  
**Kind**: case

The user specified that the certificate should not be trusted.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case deny
```

#### Discussion

This value indicates that the user explicitly chose to not trust a certificate in the chain, usually by clicking the appropriate button in a certificate trust panel. Your app should  trust the chain. The Keychain Access utility refers to this value as “Never Trust.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustresulttype/deny)*