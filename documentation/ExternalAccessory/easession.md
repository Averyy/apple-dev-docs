# EASession

**Framework**: External Accessory  
**Kind**: class

The object you use to manage communications between your app and a connected hardware accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class EASession
```

#### Overview

An [`EASession`](easession.md) object creates a communications channel between your app and a connected hardware accessory. The manufacturer of the device must share the accessory’s supported protocols with you. When you create your session, specify one of these protocols to initiate communication with the accessory. After initializing an [`EASession`](easession.md) object, use the provided output and input streams to transfer data to and from the accessory using that protocol.

After creating a session object, immediately retrieve and configure the stream objects provided by the session. Streams send events to their associated delegate to notify it of changes in the stream status. For example, streams notify the delegate when data is waiting to be read or when more space is available for writing data. For more information about how to use stream objects, see [`Stream Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i).

When sending and receiving data using the provided streams, it is your responsibility to ensure the data is formatted according to the specified protocol. The [`EASession`](easession.md) class has no knowledge of specific accessory protocols and doesn’t attempt to format the data in any way before or after transferring it.

## Topics

### Creating the Session Object
- [init?(accessory: EAAccessory, forProtocol: String)](easession/init(accessory:forprotocol:).md)
  Initializes the session for the specified accessory and protocol.
### Getting Session Information
- [var accessory: EAAccessory?](easession/accessory.md)
  The accessory attached to the session.
- [var protocolString: String?](easession/protocolstring.md)
  The protocol being used for communication with the accessory.
### Getting the Communication Streams
- [var inputStream: InputStream?](easession/inputstream.md)
  The stream to use for receiving data from the accessory.
- [var outputStream: OutputStream?](easession/outputstream.md)
  The stream to use for sending data to the accessory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class EAAccessory](eaaccessory.md)
  An object that contains information about a single, connected hardware accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/easession)*