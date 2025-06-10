# next(isolation:)

**Framework**: Swift  
**Kind**: method

Advances to and returns the result of the next child task.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Failure) -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator.Element?
```

#### Return Value

The value returned by the next child task that completes, or `nil` if there are no remaining child tasks,

#### Discussion

The elements returned from this method appear in the order that the tasks , not in the order that those tasks were added to the task group. After this method returns `nil`, this iterator is guaranteed to never produce more values.

For more information about the iteration order and semantics, see `ThrowingTaskGroup.next()`

> **Note**: The error thrown by the next child task that completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/iterator/next(isolation:))*