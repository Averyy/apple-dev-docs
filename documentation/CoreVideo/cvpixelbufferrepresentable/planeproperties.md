# planeProperties

**Framework**: Core Video  
**Kind**: property

Properties of all the planes in this pixel buffer. This array will contain at least one element. In case of non-planar pixel buffers, the first value represents the entire pixel data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var planeProperties: [CVPixelBufferPlaneProperties] { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable/planeproperties)*