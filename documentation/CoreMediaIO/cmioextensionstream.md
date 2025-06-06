# CMIOExtensionStream

**Framework**: Core Media I/O  
**Kind**: class

An object that represents a stream of media data.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStream
```

## Mentions

- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)

#### Overview

A stream delivers media samples to or from a [`CMIOExtensionDevice`](cmioextensiondevice.md).

## Topics

### Creating a Stream
- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, clockType: CMIOExtensionStream.ClockType, source: any CMIOExtensionStreamSource)](cmioextensionstream/init(localizedname:streamid:direction:clocktype:source:).md)
  Creates a stream.
- [init(localizedName: String, streamID: UUID, direction: CMIOExtensionStream.Direction, customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration, source: any CMIOExtensionStreamSource)](cmioextensionstream/init(localizedname:streamid:direction:customclockconfiguration:source:).md)
  Creates a stream that uses a custom clock configuration.
### Identifying a Stream
- [var localizedName: String](cmioextensionstream/localizedname.md)
  A localized name for the stream.
- [var streamID: UUID](cmioextensionstream/streamid.md)
  A universally unique identifier for the stream.
### Accessing Clients
- [var streamingClients: [CMIOExtensionClient]](cmioextensionstream/streamingclients.md)
  An array of clients of the stream.
### Inspecting a Stream
- [var source: (any CMIOExtensionStreamSource)?](cmioextensionstream/source.md)
  The source object for the stream.
- [var direction: CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.property.md)
  The data-flow direction of the stream.
- [CMIOExtensionStream.Direction](cmioextensionstream/direction-swift.enum.md)
  Constants that define the data-flow direction of the stream.
- [var clockType: CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.property.md)
  A clock type for the stream.
- [CMIOExtensionStream.ClockType](cmioextensionstream/clocktype-swift.enum.md)
  Constants that indicate the clock type of a stream.
- [var customClockConfiguration: CMIOExtensionStreamCustomClockConfiguration?](cmioextensionstream/customclockconfiguration.md)
  An optional custom clock configuration for a stream.
- [class CMIOExtensionStreamCustomClockConfiguration](cmioextensionstreamcustomclockconfiguration.md)
  An object that describes the parameters to create a custom clock on the host side.
### Processing Data
- [func consumeSampleBuffer(from: CMIOExtensionClient, completionHandler: (CMSampleBuffer?, UInt64, CMIOExtensionStream.DiscontinuityFlags, Bool, (any Error)?) -> Void)](cmioextensionstream/consumesamplebuffer(from:completionhandler:).md)
  Consumes a sample buffer from a client.
- [func send(CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)](cmioextensionstream/send(_:discontinuity:hosttimeinnanoseconds:).md)
  Sends a media sample to stream client.
- [CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags.md)
  Constants that specify the types of discontinuities that can occur in a media stream.
### Posting Property Changes
- [func notifyPropertiesChanged([CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensionstream/notifypropertieschanged(_:).md)
  Notifies clients about stream property changes.
### Managing Scheduled Output
- [func notifyScheduledOutputChanged(CMIOExtensionScheduledOutput)](cmioextensionstream/notifyscheduledoutputchanged(_:).md)
  Notifies clients when a particular buffer is output.
- [class CMIOExtensionScheduledOutput](cmioextensionscheduledoutput.md)
  An object that represents scheduled output.

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

- [protocol CMIOExtensionStreamSource](cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionStreamProperties](cmioextensionstreamproperties.md)
  An object that describes the properties of an extension stream.
- [class CMIOExtensionClient](cmioextensionclient.md)
  An object that represents a client of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream)*