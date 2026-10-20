# isEmpty

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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

### Accessing Individual Results
- [func next() async throws -> ChildTaskResult?](./next%28%29.md)
- [func nextResult() async -> Result<ChildTaskResult, Failure>?](./nextresult%28%29.md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [func next(isolation: isolated (any Actor)?) async throws -> ChildTaskResult?](./next%28isolation%29.md)
  Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [func waitForAll() async throws](./waitforall%28%29.md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/isempty)*