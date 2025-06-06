# affectedStores

**Framework**: Core Data  
**Kind**: property

An array of persistent stores specified for the fetch request.

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
var affectedStores: [NSPersistentStore]? { get set }
```

#### Discussion

The contents of the array are the identifiers for the stores to be searched when the fetch request is executed.

## See Also

- [var predicate: NSPredicate?](nsfetchrequest/predicate.md)
  The predicate of the fetch request.
- [var fetchLimit: Int](nsfetchrequest/fetchlimit.md)
  The fetch limit of the fetch request.
- [var fetchOffset: Int](nsfetchrequest/fetchoffset.md)
  The fetch offset of the fetch request.
- [var fetchBatchSize: Int](nsfetchrequest/fetchbatchsize.md)
  The batch size of the objects specified in the fetch request.
- [class NSFetchRequestExpression](nsfetchrequestexpression.md)
  An expression that evaluates the result of a fetch request on a managed object context.
- [class NSExpressionDescription](nsexpressiondescription.md)
  An object that describes an expression to include with a fetch request.
- [class NSFetchedPropertyDescription](nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/affectedstores)*