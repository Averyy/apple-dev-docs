# nextResult(isolation:)

**Framework**: Swift  
**Kind**: method

Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.

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
mutating func nextResult(isolation: isolated (any Actor)? = #isolation) async -> Result<ChildTaskResult, Failure>?
```

#### Return Value

A `Result.success` value containing the value that the child task returned, or a `Result.failure` value containing the error that the child task threw.

#### Discussion

The values returned by successive calls to this method appear in the order that the tasks , not in the order that those tasks were added to the task group. For example:

```swift
group.addTask { 1 }
group.addTask { 2 }

guard let result = await group.nextResult() else {
    return  // No task to wait on, which won't happen in this example.
}

switch result {
case .success(let value): print(value)
case .failure(let error): print("Failure: \(error)")
}
// Prints either "2" or "1".
```

If the next child task throws an error and you propagate that error from this method out of the body of a call to the `ThrowingTaskGroup.withThrowingTaskGroup(of:returning:body:)` method, then all remaining child tasks in that group are implicitly canceled.

> **Note**: `next()`

## See Also

- [func next() async throws -> ChildTaskResult?](throwingtaskgroup/next.md)
- [func next(isolation: isolated (any Actor)?) async throws -> ChildTaskResult?](throwingtaskgroup/next(isolation:).md)
  Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [var isEmpty: Bool](throwingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
- [func waitForAll(isolation: isolated (any Actor)?) async throws](throwingtaskgroup/waitforall(isolation:).md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/nextresult(isolation:))*