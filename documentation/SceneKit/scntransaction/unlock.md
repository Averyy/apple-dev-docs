# unlock()

**Framework**: SceneKit  
**Kind**: method

Relinquishes a previously acquired transaction lock.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func unlock()
```

#### Discussion

See the [`lock()`](scntransaction/lock().md) method for more details on transaction locking.

## See Also

- [class func lock()](scntransaction/lock.md)
  Attempts to acquire a recursive spinlock to ensure the validity of values you retrieve during the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/unlock())*