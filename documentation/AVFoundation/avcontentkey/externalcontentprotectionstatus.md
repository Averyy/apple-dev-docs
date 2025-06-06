# externalContentProtectionStatus

**Framework**: AVFoundation  
**Kind**: property

The external protection status for the content key based on all attached displays.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var externalContentProtectionStatus: AVExternalContentProtectionStatus { get }
```

#### Discussion

This property isn’t key-value observable. Instead, use the [`contentKeySession(_:externalProtectionStatusDidChangeFor:)`](avcontentkeysessiondelegate/contentkeysession(_:externalprotectionstatusdidchangefor:).md) delegate method to monitor changes to this value.

## See Also

- [func revoke()](avcontentkey/revoke.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkey/externalcontentprotectionstatus)*