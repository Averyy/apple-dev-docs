# CMIOExtensionClient

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that represents a client of the extension.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionClient
```

```objc
@interface CMIOExtensionClient : NSObject
```

## Topics

### Identifying a Client
- [var clientID: UUID](./cmioextensionclient/clientid.md)
  A unique client identifier.
- [var pid: pid_t](./cmioextensionclient/pid.md)
  The process identifier of the client.
### Instance Properties
- [var signingID: String?](./cmioextensionclient/signingid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Streams
- [class CMIOExtensionStream](./cmioextensionstream.md)
  An object that represents a stream of media data.
- [protocol CMIOExtensionStreamSource](./cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionStreamProperties](./cmioextensionstreamproperties.md)
  An object that describes the properties of an extension stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionclient)*