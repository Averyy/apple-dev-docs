# includesPendingChanges

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether, when the fetch is executed, it matches against currently unsaved changes in the managed object context.

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
var includesPendingChanges: Bool { get set }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if when the fetch is executed, the fetch will match against currently unsaved changes in the managed object context; otherwise the value is [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If the value is [`false`](https://developer.apple.com/documentation/Swift/false), the fetch request doesn’t check unsaved changes and only returns objects that matched the predicate in the persistent store.

##### Special Considerations

A value of [`true`](https://developer.apple.com/documentation/Swift/true) is not supported in conjunction with the result type [`dictionaryResultType`](nsfetchrequestresulttype/dictionaryresulttype.md), including calculation of aggregate results (such as `max` and `min`). For dictionaries, the array returned from the fetch reflects the current state in the persistent store, and does not take into account any pending changes, insertions, or deletions in the context.

If you need to take pending changes into account for some simple aggregations like `max` and `min`, you can instead use a normal fetch request, sorted on the attribute you want, with a fetch limit of 1.

## See Also

- [var resultType: NSFetchRequestResultType](nsfetchrequest/resulttype.md)
  The result type of the fetch request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/includespendingchanges)*