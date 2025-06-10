# propertiesToFetch

**Framework**: Core Data  
**Kind**: property

A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var propertiesToFetch: [Any]? { get set }
```

#### Discussion

Property descriptions can either be instances of [`NSPropertyDescription`](nspropertydescription.md) or [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). The property descriptions may represent attributes, to-one relationships, or expressions. The name of an attribute or relationship description must match the name of a description on the fetch request’s entity.

##### Special Considerations

You must set the entity for the fetch request before setting this value; otherwise, [`NSFetchRequest`](nsfetchrequest.md) throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) exception.

This property can be set with [`managedObjectResultType`](nsfetchrequestresulttype/managedobjectresulttype.md) and thereby implement a partial faulting (whereby only some of the properties are populated) of the returned objects, as well as the [`dictionaryResultType`](nsfetchrequestresulttype/dictionaryresulttype.md) to define what properties are included in the resulting [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary).

## See Also

- [var resultType: NSFetchRequestResultType](nsfetchrequest/resulttype.md)
  The result type of the fetch request.
- [var includesPendingChanges: Bool](nsfetchrequest/includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var returnsDistinctResults: Bool](nsfetchrequest/returnsdistinctresults.md)
  A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [`propertiesToFetch`](nsfetchrequest/propertiestofetch.md).
- [var includesPropertyValues: Bool](nsfetchrequest/includespropertyvalues.md)
  A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [var shouldRefreshRefetchedObjects: Bool](nsfetchrequest/shouldrefreshrefetchedobjects.md)
  A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [var returnsObjectsAsFaults: Bool](nsfetchrequest/returnsobjectsasfaults.md)
  A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [protocol NSFetchRequestResult](nsfetchrequestresult.md)
  An abstract protocol used with parameterized fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/propertiestofetch)*