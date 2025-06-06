# includesPropertyValues

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var includesPropertyValues: Bool { get set }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/swift/true) if when the fetch is executed, property data is obtained from the persistent store; otherwise it is [`false`](https://developer.apple.com/documentation/swift/false). The default value is [`true`](https://developer.apple.com/documentation/swift/true).

You can set [`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) to [`false`](https://developer.apple.com/documentation/swift/false) to avoid creating objects to represent property values and thereby reduce memory overhead. You typically should only do so, however, if you are sure that you will not need the actual property data, or you already have the information in the row cache. Otherwise, you will incur multiple trips to the database.

During a normal fetch ([`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) is [`true`](https://developer.apple.com/documentation/swift/true)), Core Data fetches the object ID  property data for the matching records, fills the row cache with the information, and returns managed objects as faults (see [`returnsObjectsAsFaults`](nsfetchrequest/returnsobjectsasfaults.md)). Although these faults are managed objects, all of their property data still resides in the row cache until the fault is fired. When the fault is fired, Core Data retrieves the data from the row cache—there is no need to go back to the database.

If [`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) is [`false`](https://developer.apple.com/documentation/swift/false), then Core Data fetches  the object ID information for the matching records—it does not populate the row cache. Core Data still returns managed objects because it only needs managed object IDs to create faults. However, if you subsequently fire the fault, Core Data looks in the (empty) row cache, doesn’t find any data, and then goes back to the store a second time for the data.

If [`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) is [`true`](https://developer.apple.com/documentation/swift/true) and [`resultType`](nsfetchrequest/resulttype.md) is set to [`managedObjectIDResultType`](nsfetchrequestresulttype/managedobjectidresulttype.md), the properties are fetched even though they are not being presented to the application and can result in a significant performance penalty.

## See Also

- [var resultType: NSFetchRequestResultType](nsfetchrequest/resulttype.md)
  The result type of the fetch request.
- [var includesPendingChanges: Bool](nsfetchrequest/includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var propertiesToFetch: [Any]?](nsfetchrequest/propertiestofetch.md)
  A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [var returnsDistinctResults: Bool](nsfetchrequest/returnsdistinctresults.md)
  A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [`propertiesToFetch`](nsfetchrequest/propertiestofetch.md).
- [var shouldRefreshRefetchedObjects: Bool](nsfetchrequest/shouldrefreshrefetchedobjects.md)
  A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [var returnsObjectsAsFaults: Bool](nsfetchrequest/returnsobjectsasfaults.md)
  A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [protocol NSFetchRequestResult](nsfetchrequestresult.md)
  An abstract protocol used with parameterized fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/includespropertyvalues)*