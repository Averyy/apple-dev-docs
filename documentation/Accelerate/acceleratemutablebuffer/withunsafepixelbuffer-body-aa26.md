# withUnsafePixelBuffer(body:)

**Framework**: Accelerate  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
mutating func withUnsafePixelBuffer<R>(body: (vImage.PixelBuffer<vImage.Planar8>) throws -> R) rethrows -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablebuffer/withunsafepixelbuffer(body:)-aa26)*