# CKDatabase.Scope.private

**Framework**: CloudKit  
**Kind**: case

The private database.

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
case `private`
```

#### Discussion

Records in a private database:

- By default are owner readable and owner writable.
- Are not visible to the application developer via the Developer Portal.
- Are counted towards the owner’s iCloud account storage quota.

## See Also

- [CKDatabase.Scope.public](ckdatabase/scope/public.md)
  The public database.
- [CKDatabase.Scope.shared](ckdatabase/scope/shared.md)
  The shared database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/scope/private)*