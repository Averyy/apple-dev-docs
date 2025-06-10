# begin()

**Framework**: SceneKit  
**Kind**: method

Begins a new transaction for the current thread.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func begin()
```

#### Discussion

The new transaction is nested within the thread’s current transaction, if there is one.

The first time you modify the scene graph during a pass through the run loop, SceneKit automatically creates a transaction and makes it the current transaction. (SceneKit commits that transaction when the next iteration of the run loops begins.) If you call this method to create a custom transaction before modifying the scene graph, your custom transaction becomes the current transaction.

## See Also

- [class func commit()](scntransaction/commit.md)
  Commits all changes made during the current transaction.
- [class func flush()](scntransaction/flush.md)
  Applies all changes from the current automatic transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/begin())*