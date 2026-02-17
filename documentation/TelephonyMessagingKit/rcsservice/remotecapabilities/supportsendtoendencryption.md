# supportsEndToEndEncryption

**Framework**: TelephonyMessagingKit  
**Kind**: property

A Boolean value indicating whether the remote end supports end-to-end encryption.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let supportsEndToEndEncryption: Bool
```

#### Discussion

Before your app sends a message or performs a request that may be end-to-end encrypted, ensure that the remote end supports end-to-end encryption by checking this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/remotecapabilities/supportsendtoendencryption)*