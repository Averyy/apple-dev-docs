# try()

**Framework**: Foundation  
**Kind**: method

Attempts to acquire a lock and immediately returns a Boolean value that indicates whether the attempt was successful.

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
func `try`() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the lock was acquired, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func lock(before: Date) -> Bool](nslock/lock(before:).md)
  Attempts to acquire a lock before a given time and returns a Boolean value indicating whether the attempt was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslock/try())*