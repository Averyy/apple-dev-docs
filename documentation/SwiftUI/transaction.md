# Transaction

**Framework**: SwiftUI  
**Kind**: struct

The context of the current state-processing update.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Transaction
```

#### Overview

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed, plus any global values set by calling [`withTransaction(_:_:)`](withtransaction(_:_:).md) or [`withAnimation(_:_:)`](withanimation(_:_:).md).

## Topics

### Creating a transaction
- [init()](transaction/init.md)
  Creates a transaction.
- [init(animation: Animation?)](transaction/init(animation:).md)
  Creates a transaction and assigns its animation property.
### Managing animations
- [var animation: Animation?](transaction/animation.md)
  The animation, if any, associated with the current state change.
- [var disablesAnimations: Bool](transaction/disablesanimations.md)
  A Boolean value that indicates whether views should disable animations.
- [func addAnimationCompletion(criteria: AnimationCompletionCriteria, () -> Void)](transaction/addanimationcompletion(criteria:_:).md)
  Adds a completion to run when the animations created with this transaction are all complete.
### Managing window dismissal
- [var dismissBehavior: DismissBehavior](transaction/dismissbehavior.md)
  The behavior for how windows will dismiss programmatically when used in conjunction with [`DismissWindowAction`](dismisswindowaction.md).
### Getting information about a transaction
- [var isContinuous: Bool](transaction/iscontinuous.md)
  A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [var scrollTargetAnchor: UnitPoint?](transaction/scrolltargetanchor.md)
  The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [var tracksVelocity: Bool](transaction/tracksvelocity.md)
  Whether this transaction will track the velocity of any animatable properties that change.
- [subscript<K>(K.Type) -> K.Value](transaction/subscript(_:).md)
  Accesses the transaction value associated with a custom key.
### Instance Properties
- [var scrollContentOffsetAdjustmentBehavior: ScrollContentOffsetAdjustmentBehavior](transaction/scrollcontentoffsetadjustmentbehavior.md)
  The behavior a scroll view will have regarding content offset adjustments for the current transaction.
- [var scrollPositionUpdatePreservesVelocity: Bool](transaction/scrollpositionupdatepreservesvelocity.md)
  Whether a programmatic update to the scroll position of a scroll view preserves the current velocity of any active scroll of the scroll view.

## See Also

- [func withTransaction<Result>(Transaction, () throws -> Result) rethrows -> Result](withtransaction(_:_:).md)
  Executes a closure with the specified transaction and returns the result.
- [func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws -> R) rethrows -> R](withtransaction(_:_:_:).md)
  Executes a closure with the specified transaction key path and value and returns the result.
- [func transaction((inout Transaction) -> Void) -> some View](view/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](view/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](view/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol TransactionKey](transactionkey.md)
  A key for accessing values in a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction)*