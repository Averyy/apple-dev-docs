# MLCSampleMode

**Framework**: ML Compute  
**Kind**: enum

A sampling mode for an upsample layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCSampleMode
```

## Topics

### Enumeration Cases
- [MLCSampleMode.nearest](mlcsamplemode/nearest.md)
- [MLCSampleMode.linear](mlcsamplemode/linear.md)
- [var debugDescription: String](mlcsamplemode/debugdescription.md)
  A textual description of the sample mode, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcsamplemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init?(shape: [Int])](mlcupsamplelayer/init(shape:).md)
  Creates an upsample layer with the shape you specify.
- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](mlcupsamplelayer/init(shape:samplemode:alignscorners:).md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsamplemode)*