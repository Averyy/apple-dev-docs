# layerWithShape:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates an upsample layer with the shape you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) layerWithShape:(NSArray<NSNumber *> *) shape;
```

#### Return Value

An upsample layer.

## Parameters

- `shape`: An array that contains the dimensions of the result tensor.

## See Also

### Creating Upsample Layers
- [+ layerWithShape:sampleMode:alignsCorners:](./layerwithshape_samplemode_alignscorners_.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignement option you specify.
- [enum MLCSampleMode](../mlcsamplemode.md)
  A sampling mode for an upsample layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/layerwithshape:)*