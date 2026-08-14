# CTCallCenter

**Framework**: Core Telephony  
**Kind**: class

An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTCallCenter
```

## Topics

### Responding to Cellular Call Events
- [var callEventHandler: ((CTCall) -> Void)?](ctcallcenter/calleventhandler.md)
  A closure dispatched when a call changes state.
- [var currentCalls: Set<CTCall>?](ctcallcenter/currentcalls.md)
  An array representing the cellular calls in progress.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CTCarrier](ctcarrier.md)
  Information about the user’s cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network.
- [class CTCall](ctcall.md)
  An object used to identify a cellular call and determine its state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter)*