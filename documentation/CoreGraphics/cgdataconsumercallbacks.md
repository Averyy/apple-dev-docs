# CGDataConsumerCallbacks

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

A structure that contains pointers to callback functions that manage the copying of data for a data consumer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CGDataConsumerCallbacks
```

```c
struct CGDataConsumerCallbacks;
```

#### Overview

The functions specified by the `CGDataConsumerCallbacks` structure are responsible for copying data that Core Graphics sends to your consumer and for handling the consumer’s basic memory management. You supply this structure to the function [`init(info:cbks:)`](./cgdataconsumer/init%28info,cbks%29.md) to create a data consumer.

## Topics

### Initializers
- [init()](./cgdataconsumercallbacks/init%28%29.md)
- [init(putBytes: CGDataConsumerPutBytesCallback?, releaseConsumer: CGDataConsumerReleaseInfoCallback?)](./cgdataconsumercallbacks/init%28putbytes,releaseconsumer%29.md)
### Instance Properties
- [var putBytes: CGDataConsumerPutBytesCallback?](./cgdataconsumercallbacks/putbytes.md)
  A pointer to a function that copies data to the data consumer. For more information, see [`CGDataConsumerPutBytesCallback`](./cgdataconsumerputbytescallback.md).
- [var releaseConsumer: CGDataConsumerReleaseInfoCallback?](./cgdataconsumercallbacks/releaseconsumer.md)
  A pointer to a function that handles clean-up for the data consumer, or `NULL`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Creating Data Consumers
- [init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](./cgdataconsumer/init%28info,cbks%29.md)
  Creates a data consumer that uses callback functions to write data.
- [init?(url: CFURL)](./cgdataconsumer/init%28url%29.md)
  Creates a data consumer that writes data to a location specified by a URL.
- [init?(data: CFMutableData)](./cgdataconsumer/init%28data%29.md)
  Creates a data consumer that writes to a CFData object.
- [typealias CGDataConsumerPutBytesCallback](./cgdataconsumerputbytescallback.md)
  Copies data from a Core Graphics-supplied buffer into a data consumer.
- [typealias CGDataConsumerReleaseInfoCallback](./cgdataconsumerreleaseinfocallback.md)
  Releases any private data or resources associated with the data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks)*