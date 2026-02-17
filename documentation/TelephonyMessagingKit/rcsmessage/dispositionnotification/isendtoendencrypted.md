# isEndToEndEncrypted

**Framework**: TelephonyMessagingKit  
**Kind**: property

A Boolean value indicating whether this message is end-to-end encrypted.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var isEndToEndEncrypted: Bool
```

#### Discussion

For outgoing messages, this indicates whether to end-to-end encrypt the message before sending out. If the service does not support end-to-end encryption, the operation will throw [`RCSService.Error.endToEndEncryptionNotSupported`](rcsservice/error/endtoendencryptionnotsupported.md).

For incoming messages, this indicates whether the message was end-to-end encrypted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/dispositionnotification/isendtoendencrypted)*