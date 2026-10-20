# begin()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Begins a new transaction for the current thread.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func begin()
```

```objc
+ (void) begin;
```

#### Discussion

The new transaction is nested within the thread’s current transaction, if there is one.

The first time you modify the scene graph during a pass through the run loop, SceneKit automatically creates a transaction and makes it the current transaction. (SceneKit commits that transaction when the next iteration of the run loops begins.) If you call this method to create a custom transaction before modifying the scene graph, your custom transaction becomes the current transaction.

## See Also

### Creating and Committing Transactions
- [class func commit()](./commit%28%29.md)
  Commits all changes made during the current transaction.
- [class func flush()](./flush%28%29.md)
  Applies all changes from the current automatic transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/begin())*