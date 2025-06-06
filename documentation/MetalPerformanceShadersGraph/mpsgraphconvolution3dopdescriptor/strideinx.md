# strideInX

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale that maps`x`-coordinate of destination to `x`-coordinate of source.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var strideInX: Int { get set }
```

#### Discussion

Source `x`-coordinate, `sx` is computed from destination `x`-coordinate, `dx` as `sx = strideInX*dx`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/strideinx)*