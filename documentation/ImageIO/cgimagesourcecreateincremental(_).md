# CGImageSourceCreateIncremental(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern CGImageSourceRefCGImageSourceCreateIncremental(CFDictionaryRef options);
```

#### Return Value

An empty image source object. You’re responsible for releasing this type using [`CFRelease`](../CoreFoundation/cfrelease.md).

#### Discussion

This function creates an empty image source container, which you use to accumulate data downloaded in chunks from the network. To add new chunks of data to the image source, call the [`CGImageSourceUpdateDataProvider(_:_:_:)`](./cgimagesourceupdatedataprovider%28_,_,_%29.md) or [`CGImageSourceUpdateData(_:_:_:)`](./cgimagesourceupdatedata%28_,_,_%29.md) functions.

## Parameters

- `options`: A dictionary that specifies additional creation options. For a list of possible values, see [Specifying the Read Options](./cgimagesource.md#Specifying-the-Read-Options).

## See Also

### Creating an Image Source
- [func CGImageSourceCreateWithURL(CFURL, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithurl%28_,_%29.md)
  Creates an image source that reads from a location specified by a URL.
- [func CGImageSourceCreateWithData(CFData, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithdata%28_,_%29.md)
  Creates an image source that reads from a Core Foundation data object.
- [func CGImageSourceCreateWithDataProvider(CGDataProvider, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithdataprovider%28_,_%29.md)
  Creates an image source that reads data from the specified data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecreateincremental(_:))*