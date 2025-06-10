# flush()

**Framework**: SceneKit  
**Kind**: method

Applies all changes from the current automatic transaction.

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
class func flush()
```

#### Discussion

SceneKit automatically calls this method at the end of each pass through the run loop, regardless of the run loop mode. If your app does not have a run loop, you must call this method explicitly.

If the current transaction has any nested transactions that are still animating, SceneKit waits to commit the current transaction’s changes until those transactions complete.

> **Note**:  If possible, avoid calling [`flush()`](scntransaction/flush().md) explicitly. By allowing [`flush()`](scntransaction/flush().md) to execute during the run loop, your app achieves better performance, atomic screen updates are preserved, and transactions and animations that work from transaction to transaction continue to function.

## See Also

- [class func begin()](scntransaction/begin.md)
  Begins a new transaction for the current thread.
- [class func commit()](scntransaction/commit.md)
  Commits all changes made during the current transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/flush())*