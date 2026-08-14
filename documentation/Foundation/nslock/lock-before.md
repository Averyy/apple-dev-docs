# lock(before:)

**Framework**: Foundation  
**Kind**: method

Attempts to acquire a lock before a given time and returns a Boolean value indicating whether the attempt was successful.

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the lock is acquired before `limit`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The thread is blocked until the receiver acquires the lock or `limit` is reached.

## Parameters

- `limit`: The time limit for attempting to acquire a lock.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [func `try`() -> Bool](nslock/try.md)
  Attempts to acquire a lock and immediately returns a Boolean value that indicates whether the attempt was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslock/lock(before:))*