# PKVoIPPushMetadata

**Framework**: PushKit  
**Kind**: class  
**Role**: Class

An object that contains metadata about a received PushKit VoIP notification.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
class PKVoIPPushMetadata
```

```objc
@interface PKVoIPPushMetadata : NSObject
```

##### Metadata

- [`mustReport`](./pkvoippushmetadata/mustreport.md)

## Topics

### Instance Properties
- [var mustReport: Bool](./pkvoippushmetadata/mustreport.md)
  A boolean indicating whether a VoIP app must report a call or live conversation in response to receiving this VoIP notification.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkvoippushmetadata)*