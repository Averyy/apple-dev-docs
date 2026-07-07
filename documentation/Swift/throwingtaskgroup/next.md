# next()

**Framework**: Swift  
**Kind**: method

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
mutating func next() async throws -> ChildTaskResult?
```

## See Also

- [func nextResult() async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult.md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [func next(isolation: isolated (any Actor)?) async throws -> ChildTaskResult?](throwingtaskgroup/next(isolation:).md)
  Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [var isEmpty: Bool](throwingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
- [func waitForAll() async throws](throwingtaskgroup/waitforall.md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/next())*