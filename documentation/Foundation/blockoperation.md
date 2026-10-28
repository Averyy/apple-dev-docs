# BlockOperation

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSBlockOperation : NSOperation
```

## Overview

The [`BlockOperation`](./blockoperation.md) class is a concrete subclass of [`Operation`](./operation.md) that manages the concurrent execution of one or more blocks. You can use this object to execute several blocks at once without having to create separate operation objects for each. When executing more than one block, the operation itself is considered finished only when all blocks have finished executing.

Blocks added to a block operation are dispatched with default priority to an appropriate work queue. The blocks themselves should not make any assumptions about the configuration of their execution environment.

For more information about blocks, see [Blocks Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502).

## Topics

### Managing the Blocks in the Operation
- [convenience init(block: () -> Void)](./blockoperation/init%28block%29.md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [func addExecutionBlock(() -> Void)](./blockoperation/addexecutionblock%28_%29.md)
  Adds the specified block to the receiver’s list of blocks to perform.
- [var executionBlocks: [() -> Void]](./blockoperation/executionblocks.md)
  The blocks associated with the receiver.

## Relationships

### Inherits From
- [Operation](./operation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Operations
- [class OperationQueue](./operationqueue.md)
  A queue that regulates the execution of operations.
- [class Operation](./operation.md)
  An abstract class that represents the code and data associated with a single task.
- [NSInvocationOperation](./nsinvocationoperation.md)
  An operation that manages the execution of a single encapsulated task specified as an invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation)*