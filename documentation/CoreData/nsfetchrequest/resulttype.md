# resultType

**Framework**: Core Data  
**Kind**: property

The result type of the fetch request.

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
var resultType: NSFetchRequestResultType { get set }
```

#### Discussion

The default value is [`managedObjectResultType`](nsfetchrequestresulttype/managedobjectresulttype.md).

If you set the value to [`managedObjectIDResultType`](nsfetchrequestresulttype/managedobjectidresulttype.md), and do not include property values in the request, sort orderings are demoted  to “best efforts” hints.

[`includesPendingChanges`](nsfetchrequest/includespendingchanges.md) discusses with whether pending changes are taken into account when the `resultType` is set to `managedObjectResultType`.

[`includesPropertyValues`](nsfetchrequest/includespropertyvalues.md) discusses whether property values are included or not by default when the `resultType` is set to `managedObjectResultType`.

## See Also

- [var includesPendingChanges: Bool](nsfetchrequest/includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var propertiesToFetch: [Any]?](nsfetchrequest/propertiestofetch.md)
  A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/resulttype)*