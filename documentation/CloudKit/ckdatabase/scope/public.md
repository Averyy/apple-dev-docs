# CKDatabase.Scope.public

**Framework**: CloudKit  
**Kind**: case

The public database.

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
case `public`
```

#### Discussion

Records in a public database:

- By default are world readable, owner writable.
- Can be locked down by Roles, a process done in the Developer Portal, a web interface.  Roles are not present in the client API.
- Are visible to the application developer via the Developer Portal.
- Do not contribute to the owner’s iCloud account storage quota.

## See Also

- [CKDatabase.Scope.private](ckdatabase/scope/private.md)
  The private database.
- [CKDatabase.Scope.shared](ckdatabase/scope/shared.md)
  The shared database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/public)*