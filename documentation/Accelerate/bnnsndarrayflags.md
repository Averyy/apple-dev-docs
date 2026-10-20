# BNNSNDArrayFlags

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Options that control the behavior of an n-dimensional array.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSNDArrayFlags
```

```c
typedef enum { ... } BNNSNDArrayFlags;
```

## Topics

### N-Dimensional Array Flags
- [init(UInt32)](./bnnsndarrayflags/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsndarrayflags/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnsndarrayflags/rawvalue.md)
- [var BNNSNDArrayFlagBackpropAccumulate: BNNSNDArrayFlags](./bnnsndarrayflagbackpropaccumulate.md)
  A flag that indicates backpropagation adds the value of the Jacobian to the elements of this n-dimensional array.
- [var BNNSNDArrayFlagBackpropSet: BNNSNDArrayFlags](./bnnsndarrayflagbackpropset.md)
  A flag that indicates the elements of this n-dimensional array are overwritten by the Jacobian during backpropagation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarrayflags)*