# requiredFormatDescription

**Framework**: Immersive Media Support  
**Kind**: property

Result CMFormatDescription for overriding on AVMutableMovie video track, which will convert asset to ParametricImmersive asset. Use replaceFormatDescription to replace the format description on the AVMutableMovieTrack.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var requiredFormatDescription: CMFormatDescription? { get }
```

## See Also

- [var isConvertible: Bool?](parametricimmersiveassetinfo/isconvertible.md)
  Result boolean to indicate if the asset can be converted to ParametricImmersive asset or not. If opt-out computeFormatDescription in the init, this boolean shows if asset is potentially convertible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo/requiredformatdescription)*