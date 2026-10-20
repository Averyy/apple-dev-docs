# lock(before:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock before a given date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func lock(before limit: Date) -> Bool
```

```objc
- (BOOL) lockBeforeDate:(NSDate *) limit;
```

#### Return Value

[`true`](../../Swift/true.md) if the lock is acquired before `limit`, otherwise [`false`](../../Swift/false.md).

#### Discussion

The thread is blocked until the receiver acquires the lock or `limit` is reached.

## Parameters

- `limit`: The time before which the lock should be acquired.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
### Acquiring a Lock
- [func `try`() -> Bool](./try%28%29.md)
  Attempts to acquire a lock, and immediately returns a Boolean value that indicates whether the attempt was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrecursivelock/lock(before:))*