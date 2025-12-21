# contact

**Framework**: CloudKit  
**Kind**: property

A displayable `CNContact` representing the blocked user.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@NSCopying
var contact: CNContact { get }
```

#### Discussion

If the blocked identity does not exist in the user’s contacts or is not accessible, returns a newly created `CNContact`. This provides formatted blocked identity information suitable for display in the application’s UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/blockedidentity/contact)*