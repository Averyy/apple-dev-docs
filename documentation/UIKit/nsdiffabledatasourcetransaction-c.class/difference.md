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
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSOrderedCollectionDifference<id> * difference;
```

## See Also

### Accessing a transaction’s information
- [sectionTransactions](./sectiontransactions.md)
  An array of section transactions for the transaction.
- [initialSnapshot](./initialsnapshot.md)
  The snapshot before the transaction occured.
- [finalSnapshot](./finalsnapshot.md)
  The snapshot after the transaction occured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-c.class/difference)*