# BNNSLinearSamplingAlignCorners

**Framework**: Accelerate  
**Kind**: var

The align corners sampling mode.

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
var BNNSLinearSamplingAlignCorners: BNNSLinearSamplingMode { get }
```

#### Discussion

This sampling mode is the same as [`BNNSLinearSamplingStrictAlignCorners`](bnnslinearsamplingstrictaligncorners.md) unless the input grid has a size of `1`.

Given an input grid with a size of `Xin` and an output grid with a size `Xout`, this mode samples the grid using the following:

```swift
spacing = (Xin - Xin/Xout) / (Xout - 1)

grid_point[0] = (Xin-1) / 2, if Xout==1
grid_point[i] = min(Xin-1, max(0, i*spacing)), for i=0,1,...,Xout-1, if Xout!=1
```

## See Also

- [init(UInt32)](bnnslinearsamplingmode/init(_:).md)
- [init(rawValue: UInt32)](bnnslinearsamplingmode/init(rawvalue:).md)
- [var rawValue: UInt32](bnnslinearsamplingmode/rawvalue.md)
- [var BNNSLinearSamplingDefault: BNNSLinearSamplingMode](bnnslinearsamplingdefault.md)
  The default linear sampling mode.
- [var BNNSLinearSamplingUnalignCorners: BNNSLinearSamplingMode](bnnslinearsamplingunaligncorners.md)
  The unalign corners sampling mode.
- [var BNNSLinearSamplingStrictAlignCorners: BNNSLinearSamplingMode](bnnslinearsamplingstrictaligncorners.md)
  The strict align corners sampling mode.
- [var BNNSLinearSamplingOffsetCorners: BNNSLinearSamplingMode](bnnslinearsamplingoffsetcorners.md)
  The offset corners sampling mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslinearsamplingaligncorners)*