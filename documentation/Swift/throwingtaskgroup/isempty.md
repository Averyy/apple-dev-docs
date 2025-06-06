# isEmpty

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the group has any remaining tasks.

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
var isEmpty: Bool { get }
```

#### Return Value

`true` if the group has no pending tasks; otherwise `false`.

#### Discussion

At the start of the body of a `withThrowingTaskGroup(of:returning:body:)` call, the task group is always empty.

It’s guaranteed to be empty when returning from that body because a task group waits for all child tasks to complete before returning.

## See Also

- [func next() async throws -> ChildTaskResult?](throwingtaskgroup/next.md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult(isolation:).md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [func waitForAll(isolation: isolated (any Actor)?) async throws](throwingtaskgroup/waitforall(isolation:).md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/isempty)*