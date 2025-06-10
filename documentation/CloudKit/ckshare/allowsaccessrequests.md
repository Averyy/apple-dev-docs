# allowsAccessRequests

**Framework**: CloudKit  
**Kind**: property

Indicates whether uninvited users can request access to this share.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var allowsAccessRequests: Bool { get set }
```

#### Discussion

By default, allows access requests is `NO` When `YES`, uninvited users can submit an access request to the share if they discover the share URL. When `NO`, the server does not allow uninvited users to request access and does not reveal whether the share exists. This property can only be modified by the share owner or an admin. Attempting to change its value as any other participant will result in an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/allowsaccessrequests)*