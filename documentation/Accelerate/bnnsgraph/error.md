# BNNSGraph.Error

**Framework**: Accelerate  
**Kind**: enum

Error codes that a graph context throws.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
enum Error
```

## Topics

### Error codes
- [BNNSGraph.Error.unableToCreateContext](bnnsgraph/error/unabletocreatecontext.md)
  The call to the underlying context-creation function failed.
- [BNNSGraph.Error.unableToCreateGraph](bnnsgraph/error/unabletocreategraph.md)
  The call to the underlying graph-creation function failed.
- [BNNSGraph.Error.unableToExecute](bnnsgraph/error/unabletoexecute.md)
  The call to the underlying graph-execute function failed.
- [BNNSGraph.Error.unableToSetDynamicShapes](bnnsgraph/error/unabletosetdynamicshapes.md)
  The call to the underlying set dynamic shapes function failed.
### Enumeration Cases
- [BNNSGraph.Error.unableToMakeGraph(_:)](bnnsgraph/error/unabletomakegraph(_:).md)
  Indicates that the call to the underlying `BNNSGraphContextSetDynamicShapes` function failed.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/error)*