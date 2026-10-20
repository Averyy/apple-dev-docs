# BNNSNDArrayFlagBackpropSet

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

A flag that indicates the elements of this n-dimensional array are overwritten by the Jacobian during backpropagation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSNDArrayFlagBackpropSet: BNNSNDArrayFlags { get }
```

```c
BNNSNDArrayFlagBackpropSet
```

## See Also

### N-Dimensional Array Flags
- [init(UInt32)](./bnnsndarrayflags/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsndarrayflags/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnsndarrayflags/rawvalue.md)
- [var BNNSNDArrayFlagBackpropAccumulate: BNNSNDArrayFlags](./bnnsndarrayflagbackpropaccumulate.md)
  A flag that indicates backpropagation adds the value of the Jacobian to the elements of this n-dimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarrayflagbackpropset)*