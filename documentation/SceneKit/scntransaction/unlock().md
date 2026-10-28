# unlock()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Relinquishes a previously acquired transaction lock.

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
class func unlock()
```

```objc
+ (void) unlock;
```

## Discussion

See the [`lock()`](./lock%28%29.md) method for more details on transaction locking.

## See Also

### Managing Concurrency
- [class func lock()](./lock%28%29.md)
  Attempts to acquire a recursive spinlock to ensure the validity of values you retrieve during the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/unlock())*