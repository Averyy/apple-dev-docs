# MCEncryptionPreference.none

**Framework**: Multipeer Connectivity  
**Kind**: case

The session should not be encrypted.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

## See Also

- [MCEncryptionPreference.optional](mcencryptionpreference/optional.md)
  The session prefers to use encryption, but accepts unencrypted connections. A connection uses encryption when all the peers choose either [`MCEncryptionPreference.optional`](mcencryptionpreference/optional.md) or [`MCEncryptionPreference.required`](mcencryptionpreference/required.md). If some peers choose [`MCEncryptionPreference.none`](mcencryptionpreference/none.md), then the session will not be encrypted. For this reason, if some peers running your app can be configured without encryption, you should always assume that the session is unencrypted.
- [MCEncryptionPreference.required](mcencryptionpreference/required.md)
  The session requires encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/none)*