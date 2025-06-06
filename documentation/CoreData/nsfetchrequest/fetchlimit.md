# fetchLimit

**Framework**: Core Data  
**Kind**: property

The fetch limit of the fetch request.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fetchLimit: Int { get set }
```

#### Discussion

The fetch limit specifies the maximum number of objects that a request should return when executed.

If you set a fetch limit, the framework makes a best effort to improve efficiency, but does not guarantee it. For every object store except the SQL store, a fetch request executed with a fetch limit in effect simply performs an unlimited fetch and throws away the unasked for rows.

## See Also

- [var predicate: NSPredicate?](nsfetchrequest/predicate.md)
  The predicate of the fetch request.
- [var fetchOffset: Int](nsfetchrequest/fetchoffset.md)
  The fetch offset of the fetch request.
- [var fetchBatchSize: Int](nsfetchrequest/fetchbatchsize.md)
  The batch size of the objects specified in the fetch request.
- [var affectedStores: [NSPersistentStore]?](nsfetchrequest/affectedstores.md)
  An array of persistent stores specified for the fetch request.
- [class NSFetchRequestExpression](nsfetchrequestexpression.md)
  An expression that evaluates the result of a fetch request on a managed object context.
- [class NSExpressionDescription](nsexpressiondescription.md)
  An object that describes an expression to include with a fetch request.
- [class NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/fetchlimit)*