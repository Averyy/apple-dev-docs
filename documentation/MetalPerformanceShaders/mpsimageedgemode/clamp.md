# MPSImageEdgeMode.clamp

**Framework**: Metal Performance Shaders  
**Kind**: case

Out-of-bound pixels are clamped to the nearest edge pixel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case clamp
```

## See Also

- [MPSImageEdgeMode.zero](mpsimageedgemode/zero.md)
  Out-of-bound pixels are set to `(0.0, 0.0, 0.0, 1.0)` for images without an alpha channel or `(0.0, 0.0, 0.0, 0.0)` for images with an alpha channel, as defined by their pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode/clamp)*