# CTCall

**Framework**: Core Telephony  
**Kind**: class  
**Role**: Class

An object used to identify a cellular call and determine its state.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Getting call information in Core Telephony is no longer supported. Use [CallKit](../CallKit/CallKit.md) instead.

## Declaration

```swift
class CTCall
```

```objc
@interface CTCall : NSObject
```

## Topics

### Obtaining Information About a Cellular Call
- [var callID: String](./ctcall/callid.md)
  A unique identifier for the cellular call.
- [var callState: String](./ctcall/callstate.md)
  The state of the cellular call.
### Getting Cellular Call State
- [Cellular Call States](./cellular-call-states.md)
  States of cellular calls; one of dialing, incoming, connected, or disconnected.

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
- [class CTCallCenter](./ctcallcenter.md)
  An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcall)*