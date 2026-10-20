# returnsDistinctResults

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [`propertiesToFetch`](./propertiestofetch.md).

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var returnsDistinctResults: Bool { get set }
```

```objc
@property (nonatomic) BOOL returnsDistinctResults;
```

#### Discussion

This value is used only if a value has been set for [`propertiesToFetch`](./propertiestofetch.md).

This value is [`true`](../../Swift/true.md) if when the fetch is executed, it returns only distinct values for the fields specified by [`propertiesToFetch`](./propertiestofetch.md); otherwise, the value is [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md).

## See Also

### Managing How Results Are Returned
- [var resultType: NSFetchRequestResultType](./resulttype.md)
  The result type of the fetch request.
- [var includesPendingChanges: Bool](./includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var propertiesToFetch: [Any]?](./propertiestofetch.md)
  A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [var includesPropertyValues: Bool](./includespropertyvalues.md)
  A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [var shouldRefreshRefetchedObjects: Bool](./shouldrefreshrefetchedobjects.md)
  A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.
- [var returnsObjectsAsFaults: Bool](./returnsobjectsasfaults.md)
  A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [protocol NSFetchRequestResult](../nsfetchrequestresult.md)
  An abstract protocol used with parameterized fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/returnsdistinctresults)*