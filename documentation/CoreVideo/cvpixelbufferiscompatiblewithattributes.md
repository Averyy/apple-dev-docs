# CVPixelBufferIsCompatibleWithAttributes(_:_:)

**Framework**: Core Video  
**Kind**: func

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func CVPixelBufferIsCompatibleWithAttributes(_ pixelBuffer: CVPixelBuffer, _ attributes: CFDictionary?) -> Bool
```

#### Discussion

Returns true if given pixel buffer is compatible with pixelBufferAttributes dictionary.

## Parameters

- `pixelBuffer`: PixelBuffer to check for compatibility.
- `attributes`: Creation attributes which pixel buffer should have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferiscompatiblewithattributes(_:_:))*