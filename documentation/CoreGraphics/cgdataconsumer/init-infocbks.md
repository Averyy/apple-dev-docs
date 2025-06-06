# init(info:cbks:)

**Framework**: Core Graphics  
**Kind**: init

Creates a data consumer that uses callback functions to write data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)
```

#### Return Value

A new data consumer object. In Objective-C, you’re responsible for releasing this object using [`CGDataConsumerRelease`](cgdataconsumerrelease.md).

## Parameters

- `info`: A pointer to data of any type or  . When the callback is called, Core Graphics passes this pointer as the   parameter.
- `cbks`: A pointer to a structure that specifies the callback functions you implement to copy data sent to the consumer and to handle the consumer’s basic memory management. For a complete description, see  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/init(info:cbks:))*