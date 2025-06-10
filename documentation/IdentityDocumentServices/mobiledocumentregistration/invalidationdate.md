# invalidationDate

**Framework**: IdentityDocumentServices  
**Kind**: property

A date that indicates when the system needs to invalidate this registration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var invalidationDate: Date?
```

#### Discussion

Use this date when you know the expiration time period of a document. If this is `nil`, the registration never expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration/invalidationdate)*