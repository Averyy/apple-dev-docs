# init(shape:sampleMode:alignsCorners:)

**Framework**: ML Compute  
**Kind**: init

Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)
```

## Parameters

- `shape`: An array representing the dimensions of the result tensor.
- `sampleMode`: The upsampling algorithm type; the default value is nearest.
- `alignsCorners`: A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.

## See Also

- [convenience init?(shape: [Int])](mlcupsamplelayer/init(shape:).md)
  Creates an upsample layer with the shape you specify.
- [enum MLCSampleMode](mlcsamplemode.md)
  A sampling mode for an upsample layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/init(shape:samplemode:alignscorners:))*