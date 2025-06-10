# fillExtendedPixels()

**Framework**: Core Video  
**Kind**: method

Fills the extended pixels of the pixel buffer. This method replicates the edge pixels to fill the entire extended region of the image.

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
@discardableResult
mutating func fillExtendedPixels() -> Bool
```

#### Discussion

- Returns false if this operation is not supported by the pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/fillextendedpixels())*