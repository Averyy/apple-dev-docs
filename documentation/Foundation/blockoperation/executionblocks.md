# executionBlocks

**Framework**: Foundation  
**Kind**: property

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
var executionBlocks: [() -> Void] { get }
```

#### Discussion

The blocks in this array are copies of those originally added using the [`addExecutionBlock(_:)`](blockoperation/addexecutionblock(_:).md) method.

## See Also

- [convenience init(block: () -> Void)](blockoperation/init(block:).md)
  Creates and returns an `NSBlockOperation` object and adds the specified block to it.
- [func addExecutionBlock(() -> Void)](blockoperation/addexecutionblock(_:).md)
  Adds the specified block to the receiver’s list of blocks to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/blockoperation/executionblocks)*