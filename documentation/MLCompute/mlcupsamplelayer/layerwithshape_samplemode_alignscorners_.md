# layerWithShape:sampleMode:alignsCorners:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates an upsample layer with the shape, upsampling algorithm, and corner alignement option you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) layerWithShape:(NSArray<NSNumber *> *) shape sampleMode:(MLCSampleMode) sampleMode alignsCorners:(BOOL) alignsCorners;
```

#### Return Value

An upsample layer.

## Parameters

- `shape`: An array representing the dimensions of the result tensor.
- `sampleMode`: The upsampling algorithm type; the default value is nearest.
- `alignsCorners`: A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.

## See Also

### Creating Upsample Layers
- [+ layerWithShape:](./layerwithshape_.md)
  Creates an upsample layer with the shape you specify.
- [enum MLCSampleMode](../mlcsamplemode.md)
  A sampling mode for an upsample layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/layerwithshape:samplemode:alignscorners:)*