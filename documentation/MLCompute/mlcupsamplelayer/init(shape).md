# init(shape:)

**Framework**: ML Compute  
**Kind**: init

Creates an upsample layer with the shape you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(shape: [Int])
```

## Parameters

- `shape`: An array that contains the dimensions of the result tensor.

## See Also

- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](mlcupsamplelayer/init(shape:samplemode:alignscorners:).md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.
- [enum MLCSampleMode](mlcsamplemode.md)
  A sampling mode for an upsample layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/init(shape:))*