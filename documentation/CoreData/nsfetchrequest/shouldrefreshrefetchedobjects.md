# shouldRefreshRefetchedObjects

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the property values of fetched objects will be updated with the current values in the persistent store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shouldRefreshRefetchedObjects: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldRefreshRefetchedObjects;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the property values of fetched objects will be updated with the current values in the persistent store; otherwise, it is [`false`](../../Swift/false.md).

By default when you fetch objects, they maintain their current property values, even if the values in the persistent store have changed. Invoking this method with the parameter [`true`](../../Swift/true.md) means that when the fetch is executed, the property values of fetched objects are updated with the current values in the persistent store. This is a more convenient way to ensure that managed object property values are consistent with the store than by using [`refresh(_:mergeChanges:)`](../nsmanagedobjectcontext/refresh%28_,mergechanges%29.md) (`NSManagedObjetContext`) for multiple objects in turn.

## See Also

### Managing How Results Are Returned
- [var resultType: NSFetchRequestResultType](./resulttype.md)
  The result type of the fetch request.
- [var includesPendingChanges: Bool](./includespendingchanges.md)
  A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.
- [var propertiesToFetch: [Any]?](./propertiestofetch.md)
  A collection of either property descriptions or string property names that specify which properties should be returned by the fetch.
- [var returnsDistinctResults: Bool](./returnsdistinctresults.md)
  A Boolean value that indicates whether the fetch request returns only distinct values for the fields specified by [`propertiesToFetch`](./propertiestofetch.md).
- [var includesPropertyValues: Bool](./includespropertyvalues.md)
  A Boolean value that indicates whether, when the fetch is executed, property data is obtained from the persistent store.
- [var returnsObjectsAsFaults: Bool](./returnsobjectsasfaults.md)
  A Boolean value that indicates whether the objects resulting from a fetch request are faults.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [protocol NSFetchRequestResult](../nsfetchrequestresult.md)
  An abstract protocol used with parameterized fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/shouldrefreshrefetchedobjects)*