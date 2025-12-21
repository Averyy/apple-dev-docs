# allowsAccessRequests

**Framework**: CloudKit  
**Kind**: property

Indicates whether uninvited users can request access to this share.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var allowsAccessRequests: Bool { get set }
```

#### Discussion

By default, this property is set to `NO`. When set to `YES`, uninvited users can request access to the share if they discover the share URL. When set to `NO`, the server prevents uninvited users from requesting access and does not indicate whether the share exists.

Only the share owner or an administrator can modify this property. Attempts by other participants to modify this property result in an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/allowsaccessrequests)*