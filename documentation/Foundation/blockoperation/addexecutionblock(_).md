# addExecutionBlock(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the specified block to the receiver’s list of blocks to perform.

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
func addExecutionBlock(_ block: @escaping @Sendable () -> Void)
```

```objc
- (void) addExecutionBlock:(void (^)()) block;
```

## Discussion

The specified block should not make any assumptions about its execution environment.

Calling this method while the receiver is executing or has already finished causes an `NSInvalidArgumentException` exception to be thrown.

## Parameters

- `block`: The block to add to the receiver’s list. The block should take no parameters and have no return value.

## See Also

### Managing the Blocks in the Operation
- [convenience init(block: () -> Void)](./init%28block%29.md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [var executionBlocks: [() -> Void]](./executionblocks.md)
  The blocks associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation/addexecutionblock(_:))*