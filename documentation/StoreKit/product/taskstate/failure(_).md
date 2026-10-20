# Product.TaskState.failure(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The task failed with an error.

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
case failure(any Error)
```

## See Also

### Task states
- [Product.TaskState.loading](./loading.md)
  The task is loading the product in the background.
- [Product.TaskState.success(_:)](./success%28_%29.md)
  The task successfully loaded the product.
- [Product.TaskState.unavailable](./unavailable.md)
  The product is unavailable in the current storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/taskstate/failure(_:))*