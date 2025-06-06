# CGImageDestinationCreateWithURL(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Creates an image destination that writes image data to the specified URL.

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
func CGImageDestinationCreateWithURL(_ url: CFURL, _ type: CFString, _ count: Int, _ options: CFDictionary?) -> CGImageDestination?
```

#### Return Value

An image destination, or `NULL` if an error occurs. You are responsible for releasing this object using [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Parameters

- `url`: The URL at which to write the image data. This object overwrites any data at the specified URL.
- `type`: The uniform type identifier of the resulting image file. For a list of system-declared and third-party identifiers, see  .
- `count`: The number of images (not including thumbnail images) you want to include in the image file.
- `options`: Future options. Specify   for this parameter.

## See Also

- [func CGImageDestinationCreateWithData(CFMutableData, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithdata(_:_:_:_:).md)
  Creates an image destination that writes to a Core Foundation mutable data object.
- [func CGImageDestinationCreateWithDataConsumer(CGDataConsumer, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithdataconsumer(_:_:_:_:).md)
  Creates an image destination that writes to the specified data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationcreatewithurl(_:_:_:_:))*