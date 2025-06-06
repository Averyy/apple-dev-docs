# BlockOperation

**Framework**: Foundation  
**Kind**: class

An operation that manages the concurrent execution of one or more blocks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class BlockOperation
```

#### Overview

The [`BlockOperation`](blockoperation.md) class is a concrete subclass of [`Operation`](operation.md) that manages the concurrent execution of one or more blocks. You can use this object to execute several blocks at once without having to create separate operation objects for each. When executing more than one block, the operation itself is considered finished only when all blocks have finished executing.

Blocks added to a block operation are dispatched with default priority to an appropriate work queue. The blocks themselves should not make any assumptions about the configuration of their execution environment.

For more information about blocks, see [`Blocks Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502).

## Topics

### Managing the Blocks in the Operation
- [convenience init(block: () -> Void)](blockoperation/init(block:).md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [func addExecutionBlock(() -> Void)](blockoperation/addexecutionblock(_:).md)
  Adds the specified block to the receiver’s list of blocks to perform.
- [var executionBlocks: [() -> Void]](blockoperation/executionblocks.md)
  The blocks associated with the receiver.

## Relationships

### Inherits From
- [Operation](operation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class OperationQueue](operationqueue.md)
  A queue that regulates the execution of operations.
- [class Operation](operation.md)
  An abstract class that represents the code and data associated with a single task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation)*