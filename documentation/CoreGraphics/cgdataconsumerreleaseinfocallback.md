# CGDataConsumerReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Releases any private data or resources associated with the data consumer.

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
typealias CGDataConsumerReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(void *) CGDataConsumerReleaseInfoCallback;
```

## Discussion

When Core Graphics frees a data consumer that has an associated release function, the release function is called.

For information on how to associate your callback function with a data consumer, see [`init(info:cbks:)`](./cgdataconsumer/init%28info,cbks%29.md) and [`CGDataConsumerCallbacks`](./cgdataconsumercallbacks.md).

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(info:cbks:)`](./cgdataconsumer/init%28info,cbks%29.md).

## See Also

### Creating Data Consumers
- [init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](./cgdataconsumer/init%28info,cbks%29.md)
  Creates a data consumer that uses callback functions to write data.
- [init?(url: CFURL)](./cgdataconsumer/init%28url%29.md)
  Creates a data consumer that writes data to a location specified by a URL.
- [init?(data: CFMutableData)](./cgdataconsumer/init%28data%29.md)
  Creates a data consumer that writes to a CFData object.
- [struct CGDataConsumerCallbacks](./cgdataconsumercallbacks.md)
  A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [typealias CGDataConsumerPutBytesCallback](./cgdataconsumerputbytescallback.md)
  Copies data from a Core Graphics-supplied buffer into a data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerreleaseinfocallback)*