# dilationRateInY

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The amount by which the weights tensor expands in the `y`-direction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dilationRateInY: Int { get set }
```

#### Discussion

The weights tensor is dilated by inserting `dilationRateInY-1` zeros between consecutive values in `y`-dimension. Dilated weights tensor width is `(dilationRateInY-1)*kernelHeight+1`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/dilationrateiny)*