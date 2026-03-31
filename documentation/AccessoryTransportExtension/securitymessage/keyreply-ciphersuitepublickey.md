# SecurityMessage.keyReply(ciphersuite:publicKey:)

**Framework**: Accessory Transport Extension  
**Kind**: case

[Step 2] Extension -> Host: reply to `keyRequest` event.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
case keyReply(ciphersuite: SecurityMessage.CipherSuite, publicKey: Data)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/keyreply(ciphersuite:publickey:))*