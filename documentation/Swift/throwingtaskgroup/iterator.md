# ThrowingTaskGroup.Iterator

**Framework**: Swift  
**Kind**: struct

A type that provides an iteration interface over the results of tasks added to the group.

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
struct Iterator
```

#### Overview

The elements returned by this iterator appear in the order that the tasks , not in the order that those tasks were added to the task group.

This iterator terminates after all tasks have completed successfully, or after any task completes by throwing an error. If a task completes by throwing an error, it doesn’t return any further task results. After iterating over the results of each task, it’s valid to make a new iterator for the task group, which you can use to iterate over the results of new tasks you add to the group. You can also make a new iterator to resume iteration after a child task throws an error. For example:

```swift
group.addTask { 1 }
group.addTask { throw SomeError }
group.addTask { 2 }

do {
    // Assuming the child tasks complete in order, this prints "1"
    // and then throws an error.
    for try await r in group { print(r) }
} catch {
    // Resolve the error.
}

// Assuming the child tasks complete in order, this prints "2".
for try await r in group { print(r) }
```

> **Note**: `ThrowingTaskGroup.next()`

## Topics

### Instance Methods
- [func cancel()](throwingtaskgroup/iterator/cancel.md)
- [func next() async throws -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator.Element?](throwingtaskgroup/iterator/next.md)
  Advances to and returns the result of the next child task.
- [func next(isolation: isolated (any Actor)?) async throws(Failure) -> ThrowingTaskGroup<ChildTaskResult, Failure>.Iterator.Element?](throwingtaskgroup/iterator/next(isolation:).md)
  Advances to and returns the result of the next child task.
### Type Aliases
- [ThrowingTaskGroup.Iterator.Element](throwingtaskgroup/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](throwingtaskgroup/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)

## See Also

- [ThrowingTaskGroup.Element](throwingtaskgroup/element.md)
  The type of element produced by this asynchronous sequence.
- [ThrowingTaskGroup.AsyncIterator](throwingtaskgroup/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingtaskgroup/iterator)*