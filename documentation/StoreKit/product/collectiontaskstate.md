# Product.CollectionTaskState

**Framework**: StoreKit  
**Kind**: enum

The state of a task that loads a collection of products in the background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
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
- [Product.CollectionTaskState.loading](product/collectiontaskstate/loading.md)
  The task is loading the collection in the background.
- [Product.CollectionTaskState.success(_:unavailable:)](product/collectiontaskstate/success(_:unavailable:).md)
  The task completed loading the collection.
- [Product.CollectionTaskState.failure(_:)](product/collectiontaskstate/failure(_:).md)
  The task failed with an error.
### Instance Properties
- [var products: [Product]?](product/collectiontaskstate/products.md)
  An array of available products if the task was successful.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Product.TaskState](product/taskstate.md)
  The state of a task that loads a product in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/collectiontaskstate)*