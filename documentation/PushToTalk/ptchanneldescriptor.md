# PTChannelDescriptor

**Framework**: Push to Talk  
**Kind**: class

An object that describes a channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTChannelDescriptor
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

## Topics

### Creating a channel descriptor
- [init(name: String, image: UIImage?)](ptchanneldescriptor/init(name:image:).md)
  Creates a channel descriptor with the name and image you specify.
### Inspecting a channel descriptor
- [var name: String](ptchanneldescriptor/name.md)
  The channel name that the system presents in the system user interface.
- [var image: UIImage?](ptchanneldescriptor/image.md)
  The channel photo that the system presents in the user interface to represent the channel.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol PTChannelRestorationDelegate](ptchannelrestorationdelegate.md)
  A type that represents the channel restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchanneldescriptor)*