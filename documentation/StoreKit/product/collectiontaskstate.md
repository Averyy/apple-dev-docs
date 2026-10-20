# Product.CollectionTaskState

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The state of a task that loads a collection of products in the background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CollectionTaskState
```

## Topics

### Collection task states
- [Product.CollectionTaskState.loading](./collectiontaskstate/loading.md)
  The task is loading the collection in the background.
- [Product.CollectionTaskState.success(_:unavailable:)](./collectiontaskstate/success%28_,unavailable%29.md)
  The task completed loading the collection.
- [Product.CollectionTaskState.failure(_:)](./collectiontaskstate/failure%28_%29.md)
  The task failed with an error.
### Instance Properties
- [var products: [Product]?](./collectiontaskstate/products.md)
  An array of available products if the task was successful.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading products
- [Product.TaskState](./taskstate.md)
  The state of a task that loads a product in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/collectiontaskstate)*