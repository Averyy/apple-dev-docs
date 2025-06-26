# CVPixelFormatDescription.ComponentRange.video

**Framework**: Core Video  
**Kind**: case

Indicates that this component represents the nominal range of values in a color component using a reduced range of (usually integer) values. For example, in 8-bit YCbCr formats, video range indicates that a -1.0 to 1.0 range for chroma components is represented by the values 16 to 240, while the range of luma components is typically 16 to 235.  Values outside this range are still used for certain signaling purposes.

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
case video
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/componentrange-swift.enum/video)*