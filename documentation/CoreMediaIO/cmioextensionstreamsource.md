# CMIOExtensionStreamSource

**Framework**: Core Media I/O  
**Kind**: protocol

A protocol for objects that act as stream sources.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
protocol CMIOExtensionStreamSource : NSObjectProtocol
```

#### Overview

Create a class that adopts this protocol to configure stream properties and manage the stream life cycle.

## Topics

### Accessing the Source Format
- [var formats: [CMIOExtensionStreamFormat]](cmioextensionstreamsource/formats.md)
  An array of formats that a stream supports.
- [class CMIOExtensionStreamFormat](cmioextensionstreamformat.md)
  An object that describes the format of a media stream.
### Managing Stream Properties
- [var availableProperties: Set<CMIOExtensionProperty>](cmioextensionstreamsource/availableproperties.md)
  A set of properties available for the stream.
- [func streamProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties](cmioextensionstreamsource/streamproperties(forproperties:).md)
  Gets the states of specified properties.
- [func setStreamProperties(CMIOExtensionStreamProperties) throws](cmioextensionstreamsource/setstreamproperties(_:).md)
  Sets the property state of a stream.
### Managing a Stream
- [func authorizedToStartStream(for: CMIOExtensionClient) -> Bool](cmioextensionstreamsource/authorizedtostartstream(for:).md)
  Determines whether to authorize an app to use this stream.
- [func startStream() throws](cmioextensionstreamsource/startstream.md)
  Starts the stream of media data.
- [func stopStream() throws](cmioextensionstreamsource/stopstream.md)
  Stops the stream of media data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMIOExtensionStream](cmioextensionstream.md)
  An object that represents a stream of media data.
- [class CMIOExtensionStreamProperties](cmioextensionstreamproperties.md)
  An object that describes the properties of an extension stream.
- [class CMIOExtensionClient](cmioextensionclient.md)
  An object that represents a client of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource)*