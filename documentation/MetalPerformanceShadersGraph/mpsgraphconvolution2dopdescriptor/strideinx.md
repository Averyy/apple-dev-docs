# strideInX

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale that maps `x`-coordinate of the destination to `x`-coordinate of the source.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var strideInX: Int { get set }
```

#### Discussion

Source `x`-coordinate, `sx` is computed from destination `x`-coordinate, `dx` as `sx = strideInX*dx`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/strideinx)*