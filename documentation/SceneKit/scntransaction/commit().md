# commit()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Commits all changes made during the current transaction.

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
class func commit()
```

```objc
+ (void) commit;
```

#### Discussion

If there is no current transaction, this method has no effect.

## See Also

### Creating and Committing Transactions
- [class func begin()](./begin%28%29.md)
  Begins a new transaction for the current thread.
- [class func flush()](./flush%28%29.md)
  Applies all changes from the current automatic transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/commit())*