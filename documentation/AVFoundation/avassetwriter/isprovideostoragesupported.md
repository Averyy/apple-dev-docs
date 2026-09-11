# isProVideoStorageSupported

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the receiver supports writing to pre-allocated storage on this device for high data rate video capture formats such as ProRes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isProVideoStorageSupported: Bool { get }
```

#### Discussion

Check this value prior to setting the `usesProVideoStorage` property to avoid exceptions when pre-allocated storage is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/isprovideostoragesupported)*