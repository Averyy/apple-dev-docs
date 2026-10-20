# PTChannelDescriptor

**Framework**: Push to Talk  
**Kind**: class  
**Role**: Class

An object that describes a channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTChannelDescriptor
```

```objc
@interface PTChannelDescriptor : NSObject
```

## Mentions

- [Creating a Push to Talk app](./creating-a-push-to-talk-app.md)

## Topics

### Creating a channel descriptor
- [init(name: String, image: UIImage?)](./ptchanneldescriptor/init%28name,image%29.md)
  Creates a channel descriptor with the name and image you specify.
### Inspecting a channel descriptor
- [var name: String](./ptchanneldescriptor/name.md)
  The channel name that the system presents in the system user interface.
- [var image: UIImage?](./ptchanneldescriptor/image.md)
  The channel photo that the system presents in the user interface to represent the channel.

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

## See Also

### Channel restoration
- [protocol PTChannelRestorationDelegate](./ptchannelrestorationdelegate.md)
  A type that represents the channel restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchanneldescriptor)*