# CFStreamError

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

The structure returned by [`CFReadStreamGetError(_:)`](./cfreadstreamgeterror%28_%29.md) and [`CFWriteStreamGetError(_:)`](./cfwritestreamgeterror%28_%29.md).

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
struct CFStreamError
```

```c
typedef struct { ... } CFStreamError;
```

## Topics

### Initializers
- [init()](./cfstreamerror/init%28%29.md)
- [init(domain: CFIndex, error: Int32)](./cfstreamerror/init%28domain,error%29.md)
### Instance Properties
- [var domain: CFIndex](./cfstreamerror/domain.md)
  The error domain that should be used to interpret the error. See [`CFStreamErrorDomain`](./cfstreamerrordomain.md) for possible values.
- [var error: Int32](./cfstreamerror/error.md)
  The error code.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [struct CFStreamClientContext](./cfstreamclientcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamerror)*