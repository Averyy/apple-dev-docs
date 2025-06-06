# TaskGroup.Iterator

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

This iterator terminates after all tasks have completed. After iterating over the results of each task, it’s valid to make a new iterator for the task group, which you can use to iterate over the results of new tasks you add to the group. For example:

```swift
group.addTask { 1 }
for await r in group { print(r) }

// Add a new child task and iterate again.
group.addTask { 2 }
for await r in group { print(r) }
```

> **Note**: `TaskGroup.next()`

`TaskGroup.next()`

## Topics

### Instance Methods
- [func cancel()](taskgroup/iterator/cancel.md)
- [func next() async -> TaskGroup<ChildTaskResult>.Iterator.Element?](taskgroup/iterator/next.md)
  Advances to and returns the result of the next child task.
- [func next(isolation: isolated (any Actor)?) async -> TaskGroup<ChildTaskResult>.Iterator.Element?](taskgroup/iterator/next(isolation:).md)
  Advances to and returns the result of the next child task.
### Type Aliases
- [TaskGroup.Iterator.Element](taskgroup/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](taskgroup/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)

## See Also

- [TaskGroup.Element](taskgroup/element.md)
  The type of element produced by this asynchronous sequence.
- [TaskGroup.AsyncIterator](taskgroup/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/iterator)*