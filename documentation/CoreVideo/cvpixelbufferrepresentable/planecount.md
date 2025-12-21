# planeCount

**Framework**: Core Video  
**Kind**: property

Number of planes in this pixel buffer. This value will always be greater than 0. `planeCount` is more efficient to access than count property of `planes`. A non-planar pixel buffer implicitly defines a single plane. To check if the pixel buffer was defined with planes use [`isPlanar`](cvpixelbufferrepresentable/isplanar.md) property.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var planeCount: Int { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable/planecount)*