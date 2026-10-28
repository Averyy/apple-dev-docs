# waitForAll()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Wait for all of the group’s remaining tasks to complete.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated(nonsending)
mutating func waitForAll() async
```

## See Also

### Accessing Individual Results
- [func next() async -> ChildTaskResult?](./next%28%29.md)
- [func next(isolation: isolated (any Actor)?) async -> ChildTaskResult?](./next%28isolation%29.md)
  Waits for the next child task to complete, and returns the value it returned.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/waitforall())*