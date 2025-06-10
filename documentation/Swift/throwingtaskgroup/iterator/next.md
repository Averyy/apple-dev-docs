# next()

**Framework**: Swift  
**Kind**: method

Advances to and returns the result of the next child task.

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
mutating func next() async throws -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator.Element?
```

#### Return Value

The value returned by the next child task that completes, or `nil` if there are no remaining child tasks,

#### Discussion

The elements returned from this method appear in the order that the tasks , not in the order that those tasks were added to the task group. After this method returns `nil`, this iterator is guaranteed to never produce more values.

For more information about the iteration order and semantics, see `ThrowingTaskGroup.next()`

> **Note**: The error thrown by the next child task that completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/iterator/next())*