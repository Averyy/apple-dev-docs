# allowedDynamicRange(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new image configured with the specified allowed dynamic range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func allowedDynamicRange(_ range: Image.DynamicRange?) -> Image
```

#### Return Value

A new image.

#### Discussion

The following example enables HDR rendering for a specific image view, assuming that the image has an HDR (ITU-R 2100) color space and the output device supports it:

```swift
Image("hdr-asset").allowedDynamicRange(.high)
```

## Parameters

- `range`: The requested dynamic range, or nil to   restore the default allowed range.

## See Also

- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [struct DynamicRange](image/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/alloweddynamicrange(_:))*