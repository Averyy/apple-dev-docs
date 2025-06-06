# strideInZ

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale that maps`z`-coordinate of destination to `z`-coordinate of source.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var strideInZ: Int { get set }
```

#### Discussion

Source `z`-coordinate, `sz` is computed from destination `z`-coordinate, `dz` as `sz = strideInZ*dz`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/strideinz)*