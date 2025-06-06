# CFStreamError

**Framework**: Core Foundation  
**Kind**: struct

The structure returned by [`CFReadStreamGetError(_:)`](cfreadstreamgeterror(_:).md) and [`CFWriteStreamGetError(_:)`](cfwritestreamgeterror(_:).md).

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
struct CFStreamError
```

## Topics

### Initializers
- [init()](cfstreamerror/init.md)
- [init(domain: CFIndex, error: Int32)](cfstreamerror/init(domain:error:).md)
### Instance Properties
- [var domain: CFIndex](cfstreamerror/domain.md)
  The error domain that should be used to interpret the error. See [`CFStreamErrorDomain`](cfstreamerrordomain.md) for possible values.
- [var error: Int32](cfstreamerror/error.md)
  The error code.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CFStreamClientContext](cfstreamclientcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamerror)*