# CGDataConsumerPutBytesCallback

**Framework**: Core Graphics  
**Kind**: typealias

Copies data from a Core Graphics-supplied buffer into a data consumer.

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
typealias CGDataConsumerPutBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer, Int) -> Int
```

#### Return Value

The number of bytes copied. If no more data can be written to the consumer, you should return `0`.

#### Discussion

When Core Graphics is ready to send data to the consumer, your function is called. It should copy the specified number of bytes from `buffer` into some resource under your control—for example, a file.

For information on how to associate your callback function with a data consumer, see [`init(info:cbks:)`](cgdataconsumer/init(info:cbks:).md) and [`CGDataConsumerCallbacks`](cgdataconsumercallbacks.md).

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the pointer supplied to  .
- `buffer`: The buffer from which you copy the specified number of bytes.
- `count`: The number of bytes to copy.

## See Also

- [init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](cgdataconsumer/init(info:cbks:).md)
  Creates a data consumer that uses callback functions to write data.
- [init?(url: CFURL)](cgdataconsumer/init(url:).md)
  Creates a data consumer that writes data to a location specified by a URL.
- [init?(data: CFMutableData)](cgdataconsumer/init(data:).md)
  Creates a data consumer that writes to a CFData object.
- [struct CGDataConsumerCallbacks](cgdataconsumercallbacks.md)
  A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [typealias CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md)
  Releases any private data or resources associated with the data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerputbytescallback)*