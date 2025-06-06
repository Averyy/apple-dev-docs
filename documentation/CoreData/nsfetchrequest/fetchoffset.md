# fetchOffset

**Framework**: Core Data  
**Kind**: property

The fetch offset of the fetch request.

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
var fetchOffset: Int { get set }
```

#### Discussion

The default value is `0`.

This setting allows you to specify an offset at which rows will begin being returned. Effectively, the request skips the specified number of matching entries. For example, given a fetch that typically returns `a, b, c, d`, specifying an offset of 1 will return `b, c, d`, and an offset of 4  will return an empty array. Offsets are ignored in nested requests such as subqueries.

This property can be used to restrict the working set of data.  In combination with [`fetchLimit`](nsfetchrequest/fetchlimit.md), you can create a subrange of an arbitrary result set.

## See Also

- [var predicate: NSPredicate?](nsfetchrequest/predicate.md)
  The predicate of the fetch request.
- [var fetchLimit: Int](nsfetchrequest/fetchlimit.md)
  The fetch limit of the fetch request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/fetchoffset)*