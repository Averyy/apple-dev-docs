# contact

**Framework**: CloudKit  
**Kind**: property

Returns a displayable `CNContact` for the blocked identity, or a new `CNContact` if none exists in the user’s contacts. Provides a standardized format for the blocked identity’s underlying lookup info in the user identity. Use when displaying the blocked identity information to other participants in application UI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var contact: CNContact { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockedidentity/contact)*