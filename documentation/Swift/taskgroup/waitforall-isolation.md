# waitForAll(isolation:)

**Framework**: Swift  
**Kind**: method

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
mutating func waitForAll(isolation: isolated (any Actor)? = #isolation) async
```

## See Also

- [func next(isolation: isolated (any Actor)?) async -> ChildTaskResult?](taskgroup/next(isolation:).md)
  Waits for the next child task to complete, and returns the value it returned.
- [var isEmpty: Bool](taskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/waitforall(isolation:))*