# BNNSPaddingModeConstant

**Framework**: Accelerate  
**Kind**: var

A constant that indicates that a padding operation fills the padded area with a specified constant.

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
var BNNSPaddingModeConstant: BNNSPaddingMode { get }
```

#### Discussion

For example, given the following padding size and input:

```swift
let paddingSize = (2, 4)

let source: [Float] = [ 0, 1, 2, 3, 4, 5, 7, 8, 9 ]

var destination = [Float](repeating: 0,
                          count: source.count + paddingSize.0 + paddingSize.1)
```

A padding operation using [`BNNSPaddingModeConstant`](bnnspaddingmodeconstant.md) and a padding value of `99` populates destination with the following values:

```swift
[99.0, 99.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 8.0, 9.0, 99.0, 99.0, 99.0, 99.0]
```

## See Also

- [init(UInt32)](bnnspaddingmode/init(_:).md)
- [init(rawValue: UInt32)](bnnspaddingmode/init(rawvalue:).md)
- [var rawValue: UInt32](bnnspaddingmode/rawvalue.md)
- [var BNNSPaddingModeReflect: BNNSPaddingMode](bnnspaddingmodereflect.md)
  A constant that indicates that a padding operation fills the padded area to form an odd-symmetric pattern.
- [var BNNSPaddingModeSymmetric: BNNSPaddingMode](bnnspaddingmodesymmetric.md)
  A constant that indicates that a padding operation fills the padded area to form an even-symmetric pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspaddingmodeconstant)*