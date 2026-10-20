# EntitlementTaskState.failure(_:)

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

The task failed to load the entitlement, with an error.

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

### Getting the task state
- [EntitlementTaskState.loading](./loading.md)
  The task is loading the entitlement in the background.
- [EntitlementTaskState.success(_:)](./success%28_%29.md)
  The task successfully loaded the entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate/failure(_:))*