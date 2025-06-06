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

- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult(isolation:).md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [var isEmpty: Bool](throwingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
- [func waitForAll(isolation: isolated (any Actor)?) async throws](throwingtaskgroup/waitforall(isolation:).md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/next())*