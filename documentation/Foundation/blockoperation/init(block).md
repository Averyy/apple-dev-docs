# init(block:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns an `NSBlockOperation` object and adds the specified block to it.

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
convenience init(block: @escaping @Sendable () -> Void)
```

```objc
+ (instancetype) blockOperationWithBlock:(void (^)()) block;
```

#### Return Value

A new block operation object.

## Parameters

- `block`: The block to add to the new block operation object’s list. The block should take no parameters and have no return value.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
### Managing the Blocks in the Operation
- [func addExecutionBlock(() -> Void)](./addexecutionblock%28_%29.md)
  Adds the specified block to the receiver’s list of blocks to perform.
- [var executionBlocks: [() -> Void]](./executionblocks.md)
  The blocks associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation/init(block:))*