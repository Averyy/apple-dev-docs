# addExecutionBlock(_:)

**Framework**: Foundation  
**Kind**: method

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
func addExecutionBlock(_ block: @escaping () -> Void)
```

#### Discussion

The specified block should not make any assumptions about its execution environment.

Calling this method while the receiver is executing or has already finished causes an `NSInvalidArgumentException` exception to be thrown.

## Parameters

- `block`: The block to add to the receiver’s list. The block should take no parameters and have no return value.

## See Also

- [convenience init(block: () -> Void)](blockoperation/init(block:).md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [var executionBlocks: [() -> Void]](blockoperation/executionblocks.md)
  The blocks associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation/addexecutionblock(_:))*