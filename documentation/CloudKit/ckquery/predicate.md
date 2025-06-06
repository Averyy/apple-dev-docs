# predicate

**Framework**: CloudKit  
**Kind**: property

The predicate to use for matching records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate { get }
```

#### Discussion

A predicate contains one or more expressions that evaluate to [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false). Expressions are often value-based comparisons, but predicates support other types of operators, including string comparisons and aggregate operations. For guidelines on how to construct predicates for your queries, see [`Predicate Rules for Query Objects`](ckquery#Predicate-Rules-for-Query-Objects.md).

## See Also

- [var recordType: CKRecord.RecordType](ckquery/recordtype-6ajii.md)
  The record type to search.
- [var sortDescriptors: [NSSortDescriptor]?](ckquery/sortdescriptors.md)
  The sort descriptors for organizing the query’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/predicate)*