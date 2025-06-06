# strideInY

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The scale that maps`y`-coordinate of destination to `y`-coordinate of source.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var strideInY: Int { get set }
```

#### Discussion

Source `y`-coordinate, `sy` is computed from destination `y`-coordinate, `dy` as `sy = strideInY*dy`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/strideiny)*