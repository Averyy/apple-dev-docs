# PKPushPayload

**Framework**: PushKit  
**Kind**: class  
**Role**: Class

An object that contains information about a received PushKit notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class PKPushPayload
```

```objc
@interface PKPushPayload : NSObject
```

## Topics

### Payload Data
- [var dictionaryPayload: [AnyHashable : Any]](./pkpushpayload/dictionarypayload.md)
  The contents of the received payload.
- [var type: PKPushType](./pkpushpayload/type.md)
  The type value indicating how to interpret the payload.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushpayload)*