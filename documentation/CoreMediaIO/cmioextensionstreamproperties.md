# CMIOExtensionStreamProperties

**Framework**: Core Media I/O  
**Kind**: class

An object that describes the properties of an extension stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStreamProperties
```

## Topics

### Creating Stream Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensionstreamproperties/init(dictionary:).md)
  Creates a properties object that provides the specified properties and default states.
### Configuring Sink Properties
- [var sinkBufferQueueSize: Int?](cmioextensionstreamproperties/sinkbufferqueuesize-9b80c.md)
  The buffer queue size.
- [var sinkBuffersRequiredForStartup: Int?](cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq.md)
  The number of buffers the stream requires for startup.
- [var sinkBufferUnderrunCount: Int?](cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb.md)
  The buffer underrun count.
- [var sinkEndOfData: Int?](cmioextensionstreamproperties/sinkendofdata-8fswu.md)
  A value that indicates whether the stream has reached its end.
### Configuring Source Properties
- [var activeFormatIndex: Int?](cmioextensionstreamproperties/activeformatindex-83u7z.md)
  The index of the active format.
- [var frameDuration: CMTime?](cmioextensionstreamproperties/frameduration-4rnl9.md)
  The duration of the frame.
- [var maxFrameDuration: CMTime?](cmioextensionstreamproperties/maxframeduration-5qqg.md)
  The maximum duration of a frame.
### Managing Property State
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensionstreamproperties/propertiesdictionary.md)
  A dictionary representation of the property state.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensionstreamproperties/setpropertystate(_:forproperty:).md)
  Sets the state of the specified property.

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

- [class CMIOExtensionStream](cmioextensionstream.md)
  An object that represents a stream of media data.
- [protocol CMIOExtensionStreamSource](cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionClient](cmioextensionclient.md)
  An object that represents a client of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties)*