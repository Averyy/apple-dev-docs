# browserAccessibilityImageData(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS ?+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func browserAccessibilityImageData(_ attributes: [AnyHashable : Any]) -> CVPixelBuffer?
```

#### Return Value

A CVPixelBuffer containing the image pixel data, or NULL if this element does not represent an image or the requested pixel format is unsupported. The caller is responsible for releasing the returned pixel buffer.

#### Discussion

Returns image pixel data for this element as a CVPixelBuffer.

Supported keys: kCVPixelBufferPixelFormatTypeKey (NSNumber / OSType) — The desired pixel format, e.g. kCVPixelFormatType_32RGBA. Required. kCVPixelBufferWidthKey  (NSNumber) — Target image width in pixels. Absent means native width. kCVPixelBufferHeightKey (NSNumber) — Target image height in pixels. Absent means native height.

## Parameters

- `attributes`: A dictionary of CVPixelBuffer attributes specifying the desired format and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedata(_:))*