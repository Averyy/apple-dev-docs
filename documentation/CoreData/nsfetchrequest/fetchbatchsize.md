# fetchBatchSize

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The batch size of the objects specified in the fetch request.

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
var fetchBatchSize: Int { get set }
```

```objc
@property (nonatomic) NSUInteger fetchBatchSize;
```

## Discussion

The default value is `0`. A batch size of `0` is treated as infinite, which disables the batch fetching behavior.

If you set a nonzero batch size, the collection of objects returned when an instance of [`NSFetchRequest`](../nsfetchrequest.md) is executed is broken into batches. When the fetch is executed, the entire request is evaluated and the identities of all matching objects recorded, but only data for objects up to the `batchSize` will be fetched from the persistent store at a time. The array returned from executing the request is a proxy object that transparently fetches subsequent batches on demand. (In database terms, this is an in-memory cursor.)

You can use this feature to restrict the working set of data in your application. In combination with [`fetchLimit`](./fetchlimit.md), you can create a subrange of an arbitrary result set.

### Special Considerations

For purposes of thread safety, when the fetch is executed, consider the array proxy returned as being owned by the managed object context the request is executed against. Treat the array proxy as if it were a managed object registered with that context.

## See Also

### Specifying Fetch Constraints
- [var predicate: NSPredicate?](./predicate.md)
  The predicate of the fetch request.
- [var fetchLimit: Int](./fetchlimit.md)
  The fetch limit of the fetch request.
- [var fetchOffset: Int](./fetchoffset.md)
  The fetch offset of the fetch request.
- [var affectedStores: [NSPersistentStore]?](./affectedstores.md)
  An array of persistent stores specified for the fetch request.
- [class NSFetchRequestExpression](../nsfetchrequestexpression.md)
  An expression that evaluates the result of a fetch request on a managed object context.
- [class NSExpressionDescription](../nsexpressiondescription.md)
  An object that describes an expression to include with a fetch request.
- [class NSFetchedPropertyDescription](../nsfetchedpropertydescription.md)
  A description object used to define which properties are fetched from Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/fetchbatchsize)*