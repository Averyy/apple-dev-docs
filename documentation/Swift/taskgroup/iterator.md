# TaskGroup.Iterator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

Available when `ChildTaskResult` conforms to `Sendable`.

#### Overview

The elements returned by this iterator appear in the order that the tasks *completed*, not in the order that those tasks were added to the task group.

This iterator terminates after all tasks have completed. After iterating over the results of each task, it’s valid to make a new iterator for the task group, which you can use to iterate over the results of new tasks you add to the group. For example:

```swift
group.addTask { 1 }
for await r in group { print(r) }

// Add a new child task and iterate again.
group.addTask { 2 }
for await r in group { print(r) }
```

> **See Also**: `TaskGroup.next()`

## Topics

### Instance Methods
- [func cancel()](./iterator/cancel%28%29.md)
- [func next() async -> TaskGroup<ChildTaskResult>.Iterator.Element?](./iterator/next%28%29.md)
  Advances to and returns the result of the next child task.
- [func next(isolation: isolated (any Actor)?) async -> TaskGroup<ChildTaskResult>.Iterator.Element?](./iterator/next%28isolation%29.md)
  Advances to and returns the result of the next child task.
### Type Aliases
- [TaskGroup.Iterator.Element](./iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](./iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../asynciteratorprotocol.md)

## See Also

### Supporting Types
- [TaskGroup.Element](./element.md)
  The type of element produced by this asynchronous sequence.
- [TaskGroup.AsyncIterator](./asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/iterator)*