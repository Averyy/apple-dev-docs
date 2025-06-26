# isConvertible

**Framework**: Immersive Media Support  
**Kind**: property

A result Boolean value that indicates whether the asset can be converted to ParametricImmersive or not. If opt-out `computeFormatDescription` in the init, this boolean shows if asset is potentially convertible.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- Unknown ?+ - Deprecated

## Declaration

```swift
var isConvertible: Bool? { get }
```

## See Also

- [var requiredFormatDescription: CMFormatDescription?](parametricimmersiveassetinfo/requiredformatdescription.md)
  A result format description for overriding on AVMutableMovie video track, which will convert asset to ParametricImmersive asset. Use `replaceFormatDescription` to replace the format description on the `AVMutableMovieTrack`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/isconvertible)*