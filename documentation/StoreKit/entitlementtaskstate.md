# EntitlementTaskState

**Framework**: StoreKit  
**Kind**: enum

The state of an entitlement task.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum EntitlementTaskState<Value>
```

#### Overview

To get an entitlement task state, use [`currentEntitlementTask(for:priority:action:)`](https://developer.apple.com/documentation/SwiftUI/View/currentEntitlementTask(for:priority:action:)) or [`subscriptionStatusTask(for:priority:action:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStatusTask(for:priority:action:)) on a [`View`](https://developer.apple.com/documentation/SwiftUI/View).

## Topics

### Getting the task state
- [EntitlementTaskState.loading](entitlementtaskstate/loading.md)
  The task is loading the entitlement in the background.
- [EntitlementTaskState.success(_:)](entitlementtaskstate/success(_:).md)
  The task successfully loaded the entitlement.
- [EntitlementTaskState.failure(_:)](entitlementtaskstate/failure(_:).md)
  The task failed to load the entitlement, with an error.
### Getting the transaction with the entitlement
- [var transaction: VerificationResult<Transaction>?](entitlementtaskstate/transaction.md)
  The transaction value if the task is successful.
- [var value: Value?](entitlementtaskstate/value.md)
  The entitlement value if the task is successful.
### Helper methods
- [func flatMap<NewValue>((Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/flatmap(_:)-7gsnv.md)
  Returns a new state, mapping the entitlement value if successful.
- [func flatMap<NewValue>((Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/flatmap(_:)-66eb8.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/map(_:)-8ly3v.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/map(_:)-250dk.md)
  Returns a new state, mapping the entitlement value if successful.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](../SwiftUI/View/storeProductTask(for:priority:action:).md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View](../SwiftUI/View/storeProductsTask(for:priority:action:).md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](../SwiftUI/View/currentEntitlementTask(for:priority:action:).md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View](../SwiftUI/View/subscriptionStatusTask(for:priority:action:).md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [Product.CollectionTaskState](product/collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.
- [Product.TaskState](product/taskstate.md)
  The state of a task that loads a product in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate)*