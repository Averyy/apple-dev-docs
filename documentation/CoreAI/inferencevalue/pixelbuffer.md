# pixelBuffer

**Framework**: Core AI  
**Kind**: property

Consume this value to access the underlying pixel buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var pixelBuffer: CVMutablePixelBuffer? { get }
```

#### Return Value

The underlying pixel buffer or `nil` if this was not an image value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/pixelbuffer)*