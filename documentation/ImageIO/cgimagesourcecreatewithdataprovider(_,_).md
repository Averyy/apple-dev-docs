# CGImageSourceCreateWithDataProvider(_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Creates an image source that reads data from the specified data provider.

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
func CGImageSourceCreateWithDataProvider(_ provider: CGDataProvider, _ options: CFDictionary?) -> CGImageSource?
```

```c
extern CGImageSourceRefCGImageSourceCreateWithDataProvider(CGDataProviderRef provider, CFDictionaryRef options);
```

## Return Value

An image source. You’re responsible for releasing this type using [`CFRelease`](../CoreFoundation/cfrelease.md).

## Parameters

- `provider`: The data provider to read from. For more information on data providers, see [`CGDataProvider`](../CoreGraphics/cgdataprovider.md) and [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).
- `options`: A dictionary that specifies additional creation options. For a list of possible values, see [Specifying the Read Options](./cgimagesource.md#Specifying-the-Read-Options).

## See Also

### Creating an Image Source
- [func CGImageSourceCreateWithURL(CFURL, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithurl%28_,_%29.md)
  Creates an image source that reads from a location specified by a URL.
- [func CGImageSourceCreateWithData(CFData, CFDictionary?) -> CGImageSource?](./cgimagesourcecreatewithdata%28_,_%29.md)
  Creates an image source that reads from a Core Foundation data object.
- [func CGImageSourceCreateIncremental(CFDictionary?) -> CGImageSource](./cgimagesourcecreateincremental%28_%29.md)
  Creates an empty image source that you can use to accumulate incremental image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecreatewithdataprovider(_:_:))*