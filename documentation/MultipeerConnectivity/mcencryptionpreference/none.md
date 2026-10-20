# MCEncryptionPreference.none

**Framework**: Multipeer Connectivity  
**Kind**: case  
**Role**: Case

The session should not be encrypted.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
case none
```

```c
MCEncryptionNone
```

## See Also

### Constants
- [MCEncryptionPreference.optional](./optional.md)
  The session prefers to use encryption, but accepts unencrypted connections. A connection uses encryption when all the peers choose either [`MCEncryptionPreference.optional`](./optional.md) or [`MCEncryptionPreference.required`](./required.md). If some peers choose [`MCEncryptionPreference.none`](./none.md), then the session will not be encrypted. For this reason, if some peers running your app can be configured without encryption, you should always assume that the session is unencrypted.
- [MCEncryptionPreference.required](./required.md)
  The session requires encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/none)*