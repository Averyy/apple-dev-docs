# unlock()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Relinquishes the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func unlock()
```

```objc
- (void) unlock;
```

## Discussion

You should generally use the [`unlock()`](./unlock%28%29.md) method rather than [`break()`](./break%28%29.md) to release a lock.

An `NSGenericException` is raised if the receiver doesn’t already exist.

## See Also

### Relinquishing a Lock
- [func `break`()](./break%28%29.md)
  Forces the lock to be relinquished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/unlock())*