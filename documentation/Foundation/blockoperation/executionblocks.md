# executionBlocks

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The blocks associated with the receiver.

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
var executionBlocks: [@Sendable () -> Void] { get }
```

```objc
@property (copy, readonly) NSArray<void (^)(void)> * executionBlocks;
```

## Discussion

The blocks in this array are copies of those originally added using the [`addExecutionBlock(_:)`](./addexecutionblock%28_%29.md) method.

## See Also

### Managing the Blocks in the Operation
- [convenience init(block: () -> Void)](./init%28block%29.md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [func addExecutionBlock(() -> Void)](./addexecutionblock%28_%29.md)
  Adds the specified block to the receiver’s list of blocks to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation/executionblocks)*