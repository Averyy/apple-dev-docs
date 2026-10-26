# MLCSampleMode

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A sampling mode for an upsample layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCSampleMode
```

```c
enum MLCSampleMode : int32_t;
```

## Topics

### Enumeration Cases
- [MLCSampleMode.nearest](./mlcsamplemode/nearest.md)
- [MLCSampleMode.linear](./mlcsamplemode/linear.md)
- [var debugDescription: String](./mlcsamplemode/debugdescription.md)
  A textual description of the sample mode, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcsamplemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Upsample Layers
- [convenience init?(shape: [Int])](./mlcupsamplelayer/init%28shape%29.md)
  Creates an upsample layer with the shape you specify.
- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](./mlcupsamplelayer/init%28shape,samplemode,alignscorners%29.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.
- [+ layerWithShape:](./mlcupsamplelayer/layerwithshape_.md)
  Creates an upsample layer with the shape you specify.
- [+ layerWithShape:sampleMode:alignsCorners:](./mlcupsamplelayer/layerwithshape_samplemode_alignscorners_.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignement option you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsamplemode)*