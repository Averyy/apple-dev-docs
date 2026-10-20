# EntitlementTaskState

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The state of an entitlement task.

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
enum EntitlementTaskState<Value>
```

#### Overview

To get an entitlement task state, use [`currentEntitlementTask(for:priority:action:)`](../SwiftUI/view/currententitlementtask%28for,priority,action%29.md) or [`subscriptionStatusTask(for:priority:action:)`](../SwiftUI/view/subscriptionstatustask%28for,priority,action%29.md) on a [`View`](../SwiftUI/view.md).

## Topics

### Getting the task state
- [EntitlementTaskState.loading](./entitlementtaskstate/loading.md)
  The task is loading the entitlement in the background.
- [EntitlementTaskState.success(_:)](./entitlementtaskstate/success%28_%29.md)
  The task successfully loaded the entitlement.
- [EntitlementTaskState.failure(_:)](./entitlementtaskstate/failure%28_%29.md)
  The task failed to load the entitlement, with an error.
### Getting the transaction with the entitlement
- [var transaction: VerificationResult<Transaction>?](./entitlementtaskstate/transaction.md)
  The transaction value if the task is successful.
- [var value: Value?](./entitlementtaskstate/value.md)
  The entitlement value if the task is successful.
### Helper methods
- [func flatMap<NewValue>((Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>](./entitlementtaskstate/flatmap%28_%29-7gsnv.md)
  Returns a new state, mapping the entitlement value if successful.
- [func flatMap<NewValue>((Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>](./entitlementtaskstate/flatmap%28_%29-66eb8.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>](./entitlementtaskstate/map%28_%29-8ly3v.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>](./entitlementtaskstate/map%28_%29-250dk.md)
  Returns a new state, mapping the entitlement value if successful.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Loading StoreKit data
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View
](../SwiftUI/view/storeproducttask%28for,priority,action%29.md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View
](../SwiftUI/view/storeproductstask%28for,priority,action%29.md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View
](../SwiftUI/view/currententitlementtask%28for,priority,action%29.md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View
](../SwiftUI/view/subscriptionstatustask%28for,priority,action%29.md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [Product.CollectionTaskState](./product/collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.
- [Product.TaskState](./product/taskstate.md)
  The state of a task that loads a product in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate)*