# initWithRecordType:predicate:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a query with the specified record type and predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
- (instancetype) initWithRecordType:(CKRecordType) recordType predicate:(NSPredicate *) predicate;
```

#### Return Value

An initialized query object.

#### Discussion

You can’t change the record type and predicate of a query after you create it. If you want to search for a different set of records using a different set of search criteria, create a new query. You can add sort descriptors to the query and change them later as necessary.

You can’t query for user records, and executing a query where the record type is [`CKRecordTypeUserRecord`](../ckrecordtypeuserrecord-49k30.md) results in an error. You must fetch user records directly using their IDs.

## Parameters

- `recordType`: The type of record to search. Specify the name of one of your app’s supported record types. The method throws an exception if this parameter is `nil` or contains an empty string.
- `predicate`: The search predicate to apply to the prospective records. Only records that match the predicate criteria appear in the search results. For guidelines on how to construct predicates for your queries, see [Predicate Rules for Query Objects](../ckquery.md#Predicate-Rules-for-Query-Objects). This parameter must not be `nil`.

## See Also

### Creating a Query
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a query from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/initwithrecordtype:predicate:)*