# init(recordType:predicate:)

**Framework**: CloudKit  
**Kind**: init

Creates a query with the specified record type and predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate)
```

#### Discussion

You can’t change the record type and predicate of a query after you create it. If you want to search for a different set of records using a different set of search criteria, create a new query. You can add sort descriptors to the query and change them later as necessary.

You can’t query for user records, and executing a query where the record type is [`CKRecordTypeUserRecord`](ckrecordtypeuserrecord-49k30.md) results in an error. You must fetch user records directly using their IDs.

## Parameters

- `recordType`: The type of record to search. Specify the name of one of your app’s supported record types. The method throws an exception if this parameter is an empty string.
- `predicate`: The search predicate to apply to the prospective records. Only records that match the predicate criteria appear in the search results. For guidelines on how to construct predicates for your queries, see  .

## See Also

- [init(coder: NSCoder)](ckquery/init(coder:).md)
  Creates an operation group from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/init(recordtype:predicate:))*