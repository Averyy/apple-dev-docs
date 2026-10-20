# predicate

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The predicate to use for matching records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate { get }
```

```objc
@property (copy, readonly) NSPredicate * predicate;
```

#### Discussion

A predicate contains one or more expressions that evaluate to [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md). Expressions are often value-based comparisons, but predicates support other types of operators, including string comparisons and aggregate operations. For guidelines on how to construct predicates for your queries, see [Predicate Rules for Query Objects](../ckquery.md#Predicate-Rules-for-Query-Objects).

## See Also

### Accessing the Query Parameters
- [var recordType: CKRecord.RecordType](./recordtype-6ajii.md)
  The record type to search.
- [var sortDescriptors: [NSSortDescriptor]?](./sortdescriptors.md)
  The sort descriptors for organizing the query’s results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/predicate)*