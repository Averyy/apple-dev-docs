# bounds

**Framework**: AVFoundation  
**Kind**: property

The bounding rectangle associated with the metadata.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

The bounding rectangle is specified relative to the picture or video of the corresponding media. The rectangle’s origin is always specified in the top-left corner, and the x and y axis extend down and to the right.

If the metadata has no bounding rectangle, the value of this property should be [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero).

For video content, the bounding rectangle may be expressed using scalar values in the range 0.0 to 1.0. Scalar values remain meaningful even when the original video has been scaled down.

## See Also

- [var time: CMTime](avmetadataobject/time.md)
  The media time value associated with the metadata object.
- [var duration: CMTime](avmetadataobject/duration.md)
  The duration of the media associated with this metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/bounds)*