# sortDescriptors

**Framework**: CloudKit  
**Kind**: property

The sort descriptors for organizing the query’s results.

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
var sortDescriptors: [NSSortDescriptor]? { get set }
```

#### Discussion

You can add sort descriptors to a query and change them later as necessary. Each sort descriptor contains a field name of the intended record type and information about whether to sort values in that field in ascending or descending order. The default value of this property is `nil`, which means that records return in an indeterminate order.

The order of the items in the array defines the order that CloudKit applies the sort descriptors to the results. In other words, CloudKit applies the first sort descriptor in the array, then the second sort descriptor, if necessary, then the third, and so on.

## See Also

- [var recordType: CKRecord.RecordType](ckquery/recordtype-6ajii.md)
  The record type to search.
- [var predicate: NSPredicate](ckquery/predicate.md)
  The predicate to use for matching records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/sortdescriptors)*