# hasiCloudAccount

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (assign, readonly) BOOL hasiCloudAccount;
```

## Discussion

`true` if the user identity has an iCloud account; otherwise, `false`.

## See Also

### Accessing iCloud Information
- [var lookupInfo: CKUserIdentity.LookupInfo?](./lookupinfo-swift.property.md)
  The lookup info for retrieving the user identity.
- [CKUserIdentity.LookupInfo](./lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/hasicloudaccount)*