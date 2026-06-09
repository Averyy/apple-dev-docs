# dimensions

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The array of sizes, in elements, one for each dimension of this tensor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var dimensions: MTLTensorExtents? { get }
```

#### Discussion

For shader-bound tensors with dynamic extents, the [`rank`](mtltensorextents/rank.md) of `dimensions` corresponds to the rank the shader function specifies, and [`extentAtDimensionIndex:`](mtltensorextents/extentatdimensionindex:.md) always returns a value of -1.

For machine learning pipelines, `dimensions` corresponds to the default shape, if you provide one. Otherwise, it’s `nil` in the case of an undefined shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbinding/dimensions)*