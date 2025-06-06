# CMIOExtensionClient

**Framework**: Core Media I/O  
**Kind**: class

An object that represents a client of the extension.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionClient
```

## Topics

### Identifying a Client
- [var clientID: UUID](cmioextensionclient/clientid.md)
  A unique client identifier.
- [var pid: pid_t](cmioextensionclient/pid.md)
  The process identifier of the client.
### Instance Properties
- [var signingID: String?](cmioextensionclient/signingid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMIOExtensionStream](cmioextensionstream.md)
  An object that represents a stream of media data.
- [protocol CMIOExtensionStreamSource](cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionStreamProperties](cmioextensionstreamproperties.md)
  An object that describes the properties of an extension stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionclient)*