# unlock()

**Framework**: Foundation  
**Kind**: method

Relinquishes the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func unlock()
```

#### Discussion

You should generally use the [`unlock()`](nsdistributedlock/unlock().md) method rather than [`break()`](nsdistributedlock/break().md) to release a lock.

An `NSGenericException` is raised if the receiver doesn’t already exist.

## See Also

- [func `break`()](nsdistributedlock/break.md)
  Forces the lock to be relinquished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/unlock())*