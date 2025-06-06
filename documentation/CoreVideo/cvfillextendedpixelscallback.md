# CVFillExtendedPixelsCallBack

**Framework**: Core Video  
**Kind**: typealias

Defines a pointer to a custom extended pixel-fill function, which is called whenever the system needs to pad a buffer holding your custom pixel format.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
typealias CVFillExtendedPixelsCallBack = (CVPixelBuffer, UnsafeMutableRawPointer?) -> DarwinBoolean
```

#### Return Value

If `true`, the padding was successful; otherwise, `false`.

## Parameters

- `pixelBuffer`: The pixel buffer to be padded.
- `refCon`: A pointer to application-defined data. This is the same value you stored in the   structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallback)*