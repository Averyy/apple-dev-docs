# commit()

**Framework**: SceneKit  
**Kind**: method

Commits all changes made during the current transaction.

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
class func commit()
```

#### Discussion

If there is no current transaction, this method has no effect.

## See Also

- [class func begin()](scntransaction/begin.md)
  Begins a new transaction for the current thread.
- [class func flush()](scntransaction/flush.md)
  Applies all changes from the current automatic transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/commit())*