# purchased

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The transaction belongs to the purchaser.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let purchased: Transaction.OwnershipType
```

## Mentions

- [Supporting multiseat purchases in your app](../../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../../testing-multiseat-subscriptions.md)

## See Also

### Getting ownership types
- [static let familyShared: Transaction.OwnershipType](./familyshared.md)
  The transaction belongs to a family member who benefits from the service.
- [static var assigned: Transaction.OwnershipType](./assigned.md)
  The transaction belongs to a customer who has access through an organization or group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct/purchased)*