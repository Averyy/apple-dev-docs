# BNNSConstant

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

A constant that doesn’t have a gradient.

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
var BNNSConstant: BNNSDescriptorType { get }
```

```c
BNNSConstant
```

## See Also

### Descriptor Types
- [init(UInt32)](./bnnsdescriptortype/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsdescriptortype/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnsdescriptortype/rawvalue.md)
- [var BNNSParameter: BNNSDescriptorType](./bnnsparameter.md)
  A parameter that’s trainable, such as weights or bias.
- [var BNNSSample: BNNSDescriptorType](./bnnssample.md)
  A sample such as input or output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsconstant)*