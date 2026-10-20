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
nonisolated
(nonsending) mutating func waitForAll() async throws
```

#### Discussion

If any of the tasks throw, the *first* error thrown is captured and re-thrown by this method although the task group is *not* canceled when this happens.

##### Cancelling the task group on first error

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

> **Throws**: The *first* error that was thrown by a child task during draining all the tasks. This first error is stored until all other tasks have completed, and is re-thrown afterwards.

## See Also

### Accessing Individual Results
- [func next() async throws -> ChildTaskResult?](./next%28%29.md)
- [func nextResult() async -> Result<ChildTaskResult, Failure>?](./nextresult%28%29.md)
  Wait for the next child task to complete, and return a result containing either the value that the child task returned or the error that it threw.
- [func next(isolation: isolated (any Actor)?) async throws -> ChildTaskResult?](./next%28isolation%29.md)
  Wait for the next child task to complete, and return the value it returned or rethrow the error it threw.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/waitforall())*