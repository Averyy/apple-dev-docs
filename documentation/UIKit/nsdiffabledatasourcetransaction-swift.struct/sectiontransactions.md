# sectionTransactions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of section transactions for the transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>] { get }
```

## See Also

### Accessing a transaction’s information
- [var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./initialsnapshot.md)
  The snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./finalsnapshot.md)
  The snapshot after the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](./difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/sectiontransactions)*