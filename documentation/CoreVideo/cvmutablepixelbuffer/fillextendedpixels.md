# fillExtendedPixels()

**Framework**: Core Video  
**Kind**: method

Fills the extended pixels of the pixel buffer. This method replicates the edge pixels to fill the entire extended region of the image.

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
@discardableResult
mutating func fillExtendedPixels() -> Bool
```

#### Discussion

- Returns false if this operation is not supported by the pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/fillextendedpixels())*