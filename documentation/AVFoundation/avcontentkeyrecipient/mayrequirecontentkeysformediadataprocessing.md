# mayRequireContentKeysForMediaDataProcessing

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the recipient requires decryption keys for media data to enable processing.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var mayRequireContentKeysForMediaDataProcessing: Bool { get }
```

#### Discussion

When the value is [`true`](https://developer.apple.com/documentation/Swift/true), adding the recipient to a content key session allows the recipient to use the session’s existing keys. It also enables handling of new key requests by the session’s delegate object.

## See Also

- [func contentKeySession(AVContentKeySession, didProvide: AVContentKey)](avcontentkeyrecipient/contentkeysession(_:didprovide:).md)
  Tells the recipient that a content key is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient/mayrequirecontentkeysformediadataprocessing)*