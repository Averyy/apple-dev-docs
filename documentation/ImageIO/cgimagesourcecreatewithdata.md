# CGImageSourceCreateWithData(_:_:)

**Framework**: Image I/O  
**Kind**: func

Creates an image source that reads from a Core Foundation data object.

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
func CGImageSourceCreateWithData(_ data: CFData, _ options: CFDictionary?) -> CGImageSource?
```

#### Return Value

An image source. You’re responsible for releasing this type using [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Parameters

- `data`: The data object from which to read. For more information on data objects, see  doc://com.apple.documentation/documentation/corefoundation/cfdata-rv9  (Swift),   (Objective-C), and  .
- `options`: A dictionary that specifies additional creation options. For a list of possible values, see  .

## See Also

- [func CGImageSourceCreateWithURL(CFURL, CFDictionary?) -> CGImageSource?](cgimagesourcecreatewithurl(_:_:).md)
  Creates an image source that reads from a location specified by a URL.
- [func CGImageSourceCreateWithDataProvider(CGDataProvider, CFDictionary?) -> CGImageSource?](cgimagesourcecreatewithdataprovider(_:_:).md)
  Creates an image source that reads data from the specified data provider.
- [func CGImageSourceCreateIncremental(CFDictionary?) -> CGImageSource](cgimagesourcecreateincremental(_:).md)
  Creates an empty image source that you can use to accumulate incremental image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecreatewithdata(_:_:))*