# CTCallCenter

**Framework**: Core Telephony  
**Kind**: class  
**Role**: Class

An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Getting call information in Core Telephony is no longer supported. Use [CallKit](../CallKit/CallKit.md) instead.

## Declaration

```swift
class CTCallCenter
```

```objc
@interface CTCallCenter : NSObject
```

## Topics

### Responding to Cellular Call Events
- [var callEventHandler: ((CTCall) -> Void)?](./ctcallcenter/calleventhandler.md)
  A closure dispatched when a call changes state.
- [var currentCalls: Set<CTCall>?](./ctcallcenter/currentcalls.md)
  An array representing the cellular calls in progress.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated
- [class CTCarrier](./ctcarrier.md)
  Information about the user’s cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network.
- [class CTCall](./ctcall.md)
  An object used to identify a cellular call and determine its state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcallcenter)*