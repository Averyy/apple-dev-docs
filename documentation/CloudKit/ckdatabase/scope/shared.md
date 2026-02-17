# CKDatabase.Scope.shared

**Framework**: CloudKit  
**Kind**: case

The shared database.

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
case shared
```

#### Discussion

Records in a shared database:

- Are available to share participants based on the permissions of the enclosing [`CKShare`](ckshare.md)
- Are not visible to the application developer via the Developer Portal.
- Are counted towards the originating owner’s iCloud account storage quota.

## See Also

- [CKDatabase.Scope.public](ckdatabase/scope/public.md)
  The public database.
- [CKDatabase.Scope.private](ckdatabase/scope/private.md)
  The private database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/shared)*