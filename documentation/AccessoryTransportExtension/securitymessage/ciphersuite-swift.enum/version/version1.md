# SecurityMessage.CipherSuite.Version.version1

**Framework**: Accessory Transport Extension  
**Kind**: case

Version 1 of the cipher suite protocol.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case version1
```

#### Discussion

Use this value when creating [`SecurityMessage`](securitymessage.md) instances. When deriving HPKE keys on your accessory, format the protocol information as: `{cipherSuite}-version1-{identifier}`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum/version/version1)*