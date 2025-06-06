# CATransaction

**Framework**: Core Animation  
**Kind**: class

A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CATransaction
```

#### Overview

`CATransaction` is the Core Animation mechanism for batching multiple layer-tree operations into atomic updates to the render tree. Every modification to a layer tree must be part of a transaction. Nested transactions are supported.

Core Animation supports two types of transactions:  transactions and  transactions. Implicit transactions are created automatically when the layer tree is modified by a thread without an active transaction and are committed automatically when the thread’s runloop next iterates. Explicit transactions occur when the the application sends the [`CATransaction`](catransaction.md) class a [`begin()`](catransaction/begin().md) message before modifying the layer tree, and a [`commit()`](catransaction/commit().md) message afterwards.

[`CATransaction`](catransaction.md) allows you to override default animation properties that are set for animatable properties. You can customize duration, timing function, whether changes to properties trigger animations, and provide a handler that informs you when all animations from the transaction group are completed.

During a transaction you can temporarily acquire a recursive spin lock for managing property atomicity.

[`CATransaction`](catransaction.md) supports nested transactions. The following code shows how you can fade out a layer (named `transitioningLayer`) over a 2 second duration while scaling it to three times its original size. The scale animation is within a nested transaction with its own duration of 1 second. After the outer transaction completes, a completion block removes `transitioningLayer` from its parent layer.

```swift
let transitioningLayer = CALayer()
     
// Outer transaction animates `opacity` to 0 over 2 seconds
CATransaction.begin()
CATransaction.setAnimationDuration(2)
CATransaction.setCompletionBlock {
    transitioningLayer.removeFromSuperlayer()
}
    
transitioningLayer.opacity = 0
     
// Inner transaction animates scale to (3, 3, 3) over 1 second
CATransaction.begin()
CATransaction.setAnimationDuration(1)
     
transitioningLayer.transform = CATransform3DMakeScale(3, 3, 3)
     
CATransaction.commit() // Commits inner transaction
CATransaction.commit() // Commits outer transaction
```

## Topics

### Creating and Committing Transactions
- [class func begin()](catransaction/begin.md)
  Begin a new transaction for the current thread.
- [class func commit()](catransaction/commit.md)
  Commit all changes made during the current transaction.
- [class func flush()](catransaction/flush.md)
  Flushes any extant implicit transaction.
### Overriding Animation Duration and Timing
- [class func animationDuration() -> CFTimeInterval](catransaction/animationduration.md)
  Returns the animation duration used by all animations within this transaction group.
- [class func setAnimationDuration(CFTimeInterval)](catransaction/setanimationduration(_:).md)
  Sets the animation duration used by all animations within this transaction group.
- [class func animationTimingFunction() -> CAMediaTimingFunction?](catransaction/animationtimingfunction.md)
  Returns the timing function used for all animations within this transaction group.
- [class func setAnimationTimingFunction(CAMediaTimingFunction?)](catransaction/setanimationtimingfunction(_:).md)
  Sets the timing function used for all animations within this transaction group.
### Temporarily Disabling Property Animations
- [class func disableActions() -> Bool](catransaction/disableactions.md)
  Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.
- [class func setDisableActions(Bool)](catransaction/setdisableactions(_:).md)
  Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.
### Getting and Setting Completion Block Objects
- [class func completionBlock() -> (() -> Void)?](catransaction/completionblock.md)
  Returns the completion block object.
- [class func setCompletionBlock((() -> Void)?)](catransaction/setcompletionblock(_:).md)
  Sets the completion block object.
### Managing Concurrency
- [class func lock()](catransaction/lock.md)
  Attempts to acquire a recursive spin-lock lock, ensuring that returned layer values are valid until unlocked.
- [class func unlock()](catransaction/unlock.md)
  Relinquishes a previously acquired transaction lock.
### Getting and Setting Transaction Properties
- [class func setValue(Any?, forKey: String)](catransaction/setvalue(_:forkey:).md)
  Sets the arbitrary keyed-data for the specified key.
- [class func value(forKey: String) -> Any?](catransaction/value(forkey:).md)
  Returns the arbitrary keyed-data specified by the given key.
### Constants
- [Transaction properties](transaction-properties.md)
  These constants define the property keys used by [`value(forKey:)`](catransaction/value(forkey:).md) and [`setValue(_:forKey:)`](catransaction/setvalue(_:forkey:).md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CAAnimationGroup](caanimationgroup.md)
  An object that allows multiple animations to be grouped and run concurrently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction)*