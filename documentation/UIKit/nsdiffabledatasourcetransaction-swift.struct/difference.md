# difference

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A collection of insertions and removals that describe the difference between initial and final snapshots.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var difference: CollectionDifference<ItemIdentifierType> { get }
```

## See Also

### Accessing a transaction’s information
- [var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>]](./sectiontransactions.md)
  An array of section transactions for the transaction.
- [var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./initialsnapshot.md)
  The snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./finalsnapshot.md)
  The snapshot after the transaction occured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/difference)*