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
mutating func waitForAll(isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

If any of the tasks throw, the  error thrown is captured and re-thrown by this method although the task group is  cancelled when this happens.

##### Cancelling the Task Group on First Error

If you want to cancel the task group, and all “sibling” tasks, whenever any of child tasks throws an error, use the following pattern instead:

```swift
while !group.isEmpty {
    do {
        try await group.next()
    } catch is CancellationError {
        // we decide that cancellation errors thrown by children,
        // should not cause cancellation of the entire group.
        continue;
    } catch {
        // other errors though we print and cancel the group,
        // and all of the remaining child tasks within it.
        print("Error: \(error)")
        group.cancelAll()
    }
}
assert(group.isEmpty())
```

> **Note**: The  error that was thrown by a child task during draining all the tasks. This first error is stored until all other tasks have completed, and is re-thrown afterwards.

The  error that was thrown by a child task during draining all the tasks. This first error is stored until all other tasks have completed, and is re-thrown afterwards.

## See Also

- [func next() async throws -> ChildTaskResult?](throwingtaskgroup/next.md)
- [func nextResult(isolation: isolated (any Actor)?) async -> Result<ChildTaskResult, Failure>?](throwingtaskgroup/nextresult(isolation:).md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [var isEmpty: Bool](throwingtaskgroup/isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/waitforall(isolation:))*