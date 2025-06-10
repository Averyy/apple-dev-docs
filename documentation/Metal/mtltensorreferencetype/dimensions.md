# dimensions

**Framework**: Metal  
**Kind**: property

The array of sizes, in elements, one for each dimension of this tensor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var dimensions: MTLTensorExtents? { get }
```

#### Discussion

Because shader-bound tensors have dynamic extents, the [`rank`](mtltensorextents/rank.md) of `dimensions` corresponds to the rank the shader function specifies, and `MTLTensorExtents/extentsAtDimensionIndex:` always returns a value of -1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorreferencetype/dimensions)*