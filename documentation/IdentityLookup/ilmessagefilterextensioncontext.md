# ILMessageFilterExtensionContext

**Framework**: SMS and Call Reporting  
**Kind**: class

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

## Topics

### Deferring a Request to the Network
- [func deferQueryRequestToNetwork(completion: (ILNetworkResponse?, (any Error)?) -> Void)](ilmessagefilterextensioncontext/deferqueryrequesttonetwork(completion:).md)
  Tells the system to pass the current query request to the app extension’s associated network service.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ILMessageFilterExtension](ilmessagefilterextension.md)
  The abstract base class for the principal class of a Message Filter app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefilterextensioncontext)*