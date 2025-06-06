# SystemCoordinator.GroupImmersionStyles

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence that contains one or more incoming immersion styles for you to process.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct GroupImmersionStyles
```

#### Overview

When a participant in an activity changes the immersion style of their immersive space, the system adds the style to this sequence. Configure an asynchronous task to monitor this sequence and process results when they arrive.

The following example shows you how to configure this task and use it to iterate over the available items. The `systemCoordinator` variable contains the session’s [`SystemCoordinator`](SystemCoordinator.md) object.

```swift
Task.detached {
    for await immersionStyle in systemCoordinator.groupImmersionStyle {
        if let immersionStyle {
            // Open an immersive space with the same style.
        }
        else {
            // Dismiss the immersive space.
        }
    }
}
```

## Topics

### Classes
- [SystemCoordinator.GroupImmersionStyles.Iterator](systemcoordinator/groupimmersionstyles/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> SystemCoordinator.GroupImmersionStyles.Iterator](systemcoordinator/groupimmersionstyles/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [SystemCoordinator.GroupImmersionStyles.AsyncIterator](systemcoordinator/groupimmersionstyles/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [SystemCoordinator.GroupImmersionStyles.Element](systemcoordinator/groupimmersionstyles/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](systemcoordinator/groupimmersionstyles/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var groupImmersionStyle: SystemCoordinator.GroupImmersionStyles](systemcoordinator/groupimmersionstyle.md)
  The presentation style to apply to an immersive space for the current activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/groupimmersionstyles)*