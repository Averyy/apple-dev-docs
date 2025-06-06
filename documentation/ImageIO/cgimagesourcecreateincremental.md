# CGImageSourceCreateIncremental(_:)

**Framework**: Image I/O  
**Kind**: func

Creates an empty image source that you can use to accumulate incremental image data.

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
func CGImageSourceCreateIncremental(_ options: CFDictionary?) -> CGImageSource
```

#### Return Value

An empty image source object. You’re responsible for releasing this type using [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

#### Discussion

This function creates an empty image source container, which you use to accumulate data downloaded in chunks from the network. To add new chunks of data to the image source, call the [`CGImageSourceUpdateDataProvider(_:_:_:)`](cgimagesourceupdatedataprovider(_:_:_:).md) or [`CGImageSourceUpdateData(_:_:_:)`](cgimagesourceupdatedata(_:_:_:).md) functions.

## Parameters

- `options`: A dictionary that specifies additional creation options. For a list of possible values, see  .

## See Also

- [func CGImageSourceCreateWithURL(CFURL, CFDictionary?) -> CGImageSource?](cgimagesourcecreatewithurl(_:_:).md)
  Creates an image source that reads from a location specified by a URL.
- [func CGImageSourceCreateWithData(CFData, CFDictionary?) -> CGImageSource?](cgimagesourcecreatewithdata(_:_:).md)
  Creates an image source that reads from a Core Foundation data object.
- [func CGImageSourceCreateWithDataProvider(CGDataProvider, CFDictionary?) -> CGImageSource?](cgimagesourcecreatewithdataprovider(_:_:).md)
  Creates an image source that reads data from the specified data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecreateincremental(_:))*