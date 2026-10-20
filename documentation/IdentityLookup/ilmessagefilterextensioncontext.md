# ILMessageFilterExtensionContext

**Framework**: SMS and Call Reporting  
**Kind**: class  
**Role**: Class

The extension context for a Message Filter app extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
class ILMessageFilterExtensionContext
```

```objc
@interface ILMessageFilterExtensionContext : NSExtensionContext
```

## Topics

### Deferring a Request to the Network
- [func deferQueryRequestToNetwork(completion: (ILNetworkResponse?, (any Error)?) -> Void)](./ilmessagefilterextensioncontext/deferqueryrequesttonetwork%28completion%29.md)
  Tells the system to pass the current query request to the app extension’s associated network service.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App Extension
- [class ILMessageFilterExtension](./ilmessagefilterextension.md)
  The abstract base class for the principal class of a Message Filter app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterextensioncontext)*