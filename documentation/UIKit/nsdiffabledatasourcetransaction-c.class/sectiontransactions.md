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
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSDiffableDataSourceSectionTransaction<id,id> *> * sectionTransactions;
```

## See Also

### Accessing a transaction’s information
- [initialSnapshot](./initialsnapshot.md)
  The snapshot before the transaction occured.
- [finalSnapshot](./finalsnapshot.md)
  The snapshot after the transaction occured.
- [difference](./difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-c.class/sectiontransactions)*