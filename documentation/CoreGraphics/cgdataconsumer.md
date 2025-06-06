# CGDataConsumer

**Framework**: Core Graphics  
**Kind**: class

An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGDataConsumer
```

#### Overview

Most apps should use [`CGImageDestination`](https://developer.apple.com/documentation/ImageIO/CGImageDestination) objects instead.

## Topics

### Creating Data Consumers
- [init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](cgdataconsumer/init(info:cbks:).md)
  Creates a data consumer that uses callback functions to write data.
- [init?(url: CFURL)](cgdataconsumer/init(url:).md)
  Creates a data consumer that writes data to a location specified by a URL.
- [init?(data: CFMutableData)](cgdataconsumer/init(data:).md)
  Creates a data consumer that writes to a CFData object.
- [struct CGDataConsumerCallbacks](cgdataconsumercallbacks.md)
  A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [typealias CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md)
  Copies data from a Core Graphics-supplied buffer into a data consumer.
- [typealias CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md)
  Releases any private data or resources associated with the data consumer.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgdataconsumer/typeid.md)
  Returns the Core Foundation type identifier for Core Graphics data consumers.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGDataProvider](cgdataprovider.md)
  An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumer)*