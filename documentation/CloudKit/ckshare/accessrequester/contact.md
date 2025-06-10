# contact

**Framework**: CloudKit  
**Kind**: property

Returns a displayable `CNContact` for the requester, or a new `CNContact` if none exists in the user’s contacts. Provides a standardized format for the requester’s underlying lookup info in the user identity. Use when displaying the requester information to other participants and approvers in application UI.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester/contact)*