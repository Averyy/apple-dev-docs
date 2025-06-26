# blockSize

**Framework**: Core Video  
**Kind**: property

Used to assist with allocating memory for pixel formats that don’t have an integer value for bytes per pixel. Block width/height is essentially the width/height in pixels of the smallest “byte addressable” group of pixels. This works in close conjunction with [`bitsPerBlock`](cvpixelformatdescription/pixellayout/bitsperblock.md). Examples: 8-bit luminance only, blockSize.width would be 1, bitsPerBlock would be 8 16-bit 1555 RGB, blockSize.width would be 1, bitsPerBlock would be 16 32-bit 8888 ARGB, blockSize.width would be 1, bitsPerBlock would be 32 2vuy (CbYCrY), blockSize.width would be 2, bitsPerBlock would be 32 1-bit bitmap, blockSize.width would be 8, bitsPerBlock would be 8 v210, blockSize.width would be 6, bitsPerBlock would be 128

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
var blockSize: CVImageSize
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/pixellayout/blocksize)*