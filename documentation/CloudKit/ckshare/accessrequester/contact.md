# contact

**Framework**: CloudKit  
**Kind**: property

A displayable `CNContact` representing the requester.

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

If the requester doesn’t exist in the user’s contacts or is not accessible, returns a newly created `CNContact`. This provides formatted requester information suitable for display in the application’s UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/accessrequester/contact)*