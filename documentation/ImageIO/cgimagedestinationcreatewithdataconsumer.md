# CGImageDestinationCreateWithDataConsumer(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Creates an image destination that writes to the specified data consumer.

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
func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer, _ type: CFString, _ count: Int, _ options: CFDictionary?) -> CGImageDestination?
```

#### Return Value

An image destination, or `NULL` if an error occurs. You are responsible for releasing this object using [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Parameters

- `consumer`: A data consumer object to store the image data.
- `type`: The uniform type identifier of the resulting image file. For a list of system-declared and third-party identifiers, see  .
- `count`: The number of images (not including thumbnail images) you want to include in the image file.
- `options`: Future options. Specify   for this parameter.

## See Also

- [func CGImageDestinationCreateWithURL(CFURL, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithurl(_:_:_:_:).md)
  Creates an image destination that writes image data to the specified URL.
- [func CGImageDestinationCreateWithData(CFMutableData, CFString, Int, CFDictionary?) -> CGImageDestination?](cgimagedestinationcreatewithdata(_:_:_:_:).md)
  Creates an image destination that writes to a Core Foundation mutable data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationcreatewithdataconsumer(_:_:_:_:))*