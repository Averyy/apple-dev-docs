# init(blockSize:bitsPerBlock:bitsPerComponent:blockAlignment:subsampling:blackBlock:fillExtendedPixels:cgBitmapInfo:)

**Framework**: Core Video  
**Kind**: init

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
init(blockSize: CVImageSize = .init(width: 1, height: 1), bitsPerBlock: Int, bitsPerComponent: Int? = nil, blockAlignment: CVPixelFormatDescription.Dimensions = .init(horizontal: 1, vertical: 1), subsampling: CVPixelFormatDescription.Dimensions = .init(horizontal: 1, vertical: 1), blackBlock: Data? = nil, fillExtendedPixels: ((inout CVMutablePixelBuffer) -> Void)? = nil, cgBitmapInfo: CGBitmapInfo? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/pixellayout/init(blocksize:bitsperblock:bitspercomponent:blockalignment:subsampling:blackblock:fillextendedpixels:cgbitmapinfo:))*