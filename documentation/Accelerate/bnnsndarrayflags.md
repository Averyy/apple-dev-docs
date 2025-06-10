# BNNSNDArrayFlags

**Framework**: Accelerate  
**Kind**: struct

Options that control the behavior of an n-dimensional array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSNDArrayFlags
```

## Topics

### N-Dimensional Array Flags
- [init(UInt32)](bnnsndarrayflags/init(_:).md)
- [init(rawValue: UInt32)](bnnsndarrayflags/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsndarrayflags/rawvalue.md)
- [var BNNSNDArrayFlagBackpropAccumulate: BNNSNDArrayFlags](bnnsndarrayflagbackpropaccumulate.md)
  A flag that indicates backpropagation adds the value of the Jacobian to the elements of this n-dimensional array.
- [var BNNSNDArrayFlagBackpropSet: BNNSNDArrayFlags](bnnsndarrayflagbackpropset.md)
  A flag that indicates the elements of this n-dimensional array are overwritten by the Jacobian during backpropagation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarrayflags)*