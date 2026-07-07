# Product.TaskState

**Framework**: StoreKit  
**Kind**: enum

The state of a task that loads a product in the background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum TaskState
```

## Topics

### Task states
- [Product.TaskState.loading](product/taskstate/loading.md)
  The task is loading the product in the background.
- [Product.TaskState.success(_:)](product/taskstate/success(_:).md)
  The task successfully loaded the product.
- [Product.TaskState.unavailable](product/taskstate/unavailable.md)
  The product is unavailable in the current storefront.
- [Product.TaskState.failure(_:)](product/taskstate/failure(_:).md)
  The task failed with an error.
### Instance Properties
- [var product: Product?](product/taskstate/product.md)
  The product value if the task was successful.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Product.CollectionTaskState](product/collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/taskstate)*