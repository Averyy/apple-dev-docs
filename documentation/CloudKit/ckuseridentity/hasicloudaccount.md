# hasiCloudAccount

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether the user has an iCloud account.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var hasiCloudAccount: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the user identity has an iCloud account; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var lookupInfo: CKUserIdentity.LookupInfo?](ckuseridentity/lookupinfo-swift.property.md)
  The lookup info for retrieving the user identity.
- [CKUserIdentity.LookupInfo](ckuseridentity/lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/hasicloudaccount)*