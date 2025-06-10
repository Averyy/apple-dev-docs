# BNNSNDArrayFlagBackpropAccumulate

**Framework**: Accelerate  
**Kind**: var

A flag that indicates backpropagation adds the value of the Jacobian to the elements of this n-dimensional array.

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
var BNNSNDArrayFlagBackpropAccumulate: BNNSNDArrayFlags { get }
```

## See Also

- [init(UInt32)](bnnsndarrayflags/init(_:).md)
- [init(rawValue: UInt32)](bnnsndarrayflags/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsndarrayflags/rawvalue.md)
- [var BNNSNDArrayFlagBackpropSet: BNNSNDArrayFlags](bnnsndarrayflagbackpropset.md)
  A flag that indicates the elements of this n-dimensional array are overwritten by the Jacobian during backpropagation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarrayflagbackpropaccumulate)*