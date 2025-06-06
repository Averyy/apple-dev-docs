# BNNSLinearSamplingOffsetCorners

**Framework**: Accelerate  
**Kind**: var

The offset corners sampling mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var BNNSLinearSamplingOffsetCorners: BNNSLinearSamplingMode { get }
```

#### Discussion

Given an input grid with a size of `Xin` and an output grid with a size `Xout`, this mode samples the grid using the following:

```swift
delta = max(1, Xin - 1) / Xout
spacing = ((Xout - 1) * delta) / (Xout - 1)

grid_point[i] = min(Xin-1, max(0, 0.5*delta + i*spacing)), for i=0,1,...,Xout-1
```

## See Also

- [init(UInt32)](bnnslinearsamplingmode/init(_:).md)
- [init(rawValue: UInt32)](bnnslinearsamplingmode/init(rawvalue:).md)
- [var rawValue: UInt32](bnnslinearsamplingmode/rawvalue.md)
- [var BNNSLinearSamplingDefault: BNNSLinearSamplingMode](bnnslinearsamplingdefault.md)
  The default linear sampling mode.
- [var BNNSLinearSamplingAlignCorners: BNNSLinearSamplingMode](bnnslinearsamplingaligncorners.md)
  The align corners sampling mode.
- [var BNNSLinearSamplingUnalignCorners: BNNSLinearSamplingMode](bnnslinearsamplingunaligncorners.md)
  The unalign corners sampling mode.
- [var BNNSLinearSamplingStrictAlignCorners: BNNSLinearSamplingMode](bnnslinearsamplingstrictaligncorners.md)
  The strict align corners sampling mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslinearsamplingoffsetcorners)*