# lockDate

**Framework**: Foundation  
**Kind**: property

Returns the time the receiver was acquired by any of the `NSDistributedLock` objects using the same path.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var lockDate: Date { get }
```

#### Return Value

The time the receiver was acquired by any of the `NSDistributedLock` objects using the same path. Returns `nil` if the lock doesn’t exist.

#### Discussion

This method is potentially useful to applications that want to use an age heuristic to decide if a lock is too old and should be broken.

If the creation date on the lock isn’t the date on which you locked it, you’ve lost the lock: it’s been broken since you last checked it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistributedlock/lockdate)*