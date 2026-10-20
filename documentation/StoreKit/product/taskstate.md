# Product.TaskState

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The state of a task that loads a product in the background.

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
enum TaskState
```

## Topics

### Task states
- [Product.TaskState.loading](./taskstate/loading.md)
  The task is loading the product in the background.
- [Product.TaskState.success(_:)](./taskstate/success%28_%29.md)
  The task successfully loaded the product.
- [Product.TaskState.unavailable](./taskstate/unavailable.md)
  The product is unavailable in the current storefront.
- [Product.TaskState.failure(_:)](./taskstate/failure%28_%29.md)
  The task failed with an error.
### Instance Properties
- [var product: Product?](./taskstate/product.md)
  The product value if the task was successful.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading products
- [Product.CollectionTaskState](./collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/taskstate)*