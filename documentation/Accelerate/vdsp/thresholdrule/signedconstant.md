# vDSP.ThresholdRule.signedConstant(_:)

**Framework**: Accelerate  
**Kind**: case

Returns the negated constant if the input value is less than the threshold; otherwise returns the constant.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
case signedConstant(T)
```

#### Discussion

Use [`vDSP.ThresholdRule.signedConstant(_:)`](vdsp/thresholdrule/signedconstant(_:).md) to calculate a new vector where the threshold operation sets all source values below the threshold to the negated constant.

```swift
let source: [Float] = [12, 13, 14, 15, 16, 17, 18]

let destination = vDSP.threshold(source,
                                 to: 15,
                                 with: .signedConstant(99))

// Prints "[-99.0, -99.0, -99.0, 99.0, 99.0, 99.0, 99.0]".
print(destination)
```

## See Also

- [vDSP.ThresholdRule.clampToThreshold](vdsp/thresholdrule/clamptothreshold.md)
  Returns the threshold if the input value is less than threshold; otherwise returns the input value.
- [vDSP.ThresholdRule.zeroFill](vdsp/thresholdrule/zerofill.md)
  Returns `0` if the input value is less than the threshold; otherwise returns the input value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/thresholdrule/signedconstant(_:))*