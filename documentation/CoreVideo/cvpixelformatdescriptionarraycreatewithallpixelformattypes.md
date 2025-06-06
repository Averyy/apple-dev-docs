# CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_:)

**Framework**: Core Video  
**Kind**: func

Returns all the pixel format descriptions known to Core Video.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(_ allocator: CFAllocator?) -> CFArray?
```

#### Return Value

An array of Core Foundation dictionaries, each containing a pixel format description. See [`Pixel Format Description Keys`](pixel-format-description-keys.md) for a list of keys relevant to the format description.

## Parameters

- `allocator`: The allocator to use when creating the description. Pass   to specify the default allocator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescriptionarraycreatewithallpixelformattypes(_:))*