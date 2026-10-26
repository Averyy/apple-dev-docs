# CMIOExtensionStreamProperties

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that describes the properties of an extension stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStreamProperties
```

```objc
@interface CMIOExtensionStreamProperties : NSObject
```

## Topics

### Creating Stream Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./cmioextensionstreamproperties/init%28dictionary%29.md)
  Creates a properties object that provides the specified properties and default states.
- [+ streamPropertiesWithDictionary:](./cmioextensionstreamproperties/streampropertieswithdictionary_.md)
  Returns a new properties object that provides the specified properties and default states.
### Configuring Sink Properties
- [var sinkBufferQueueSize: Int?](./cmioextensionstreamproperties/sinkbufferqueuesize-9b80c.md)
  The buffer queue size.
- [var sinkBuffersRequiredForStartup: Int?](./cmioextensionstreamproperties/sinkbuffersrequiredforstartup-1bgyq.md)
  The number of buffers the stream requires for startup.
- [var sinkBufferUnderrunCount: Int?](./cmioextensionstreamproperties/sinkbufferunderruncount-1qmbb.md)
  The buffer underrun count.
- [var sinkEndOfData: Int?](./cmioextensionstreamproperties/sinkendofdata-8fswu.md)
  A value that indicates whether the stream has reached its end.
- [sinkBufferQueueSize](./cmioextensionstreamproperties/sinkbufferqueuesize-4kpug.md)
  The buffer queue size.
- [sinkBuffersRequiredForStartup](./cmioextensionstreamproperties/sinkbuffersrequiredforstartup-4b5te.md)
  The number of buffers the stream requires for startup.
- [sinkBufferUnderrunCount](./cmioextensionstreamproperties/sinkbufferunderruncount-9sph5.md)
  The buffer underrun count.
- [sinkEndOfData](./cmioextensionstreamproperties/sinkendofdata-30he9.md)
  A value that indicates whether the stream has reached its end.
### Configuring Source Properties
- [var activeFormatIndex: Int?](./cmioextensionstreamproperties/activeformatindex-83u7z.md)
  The index of the active format.
- [var frameDuration: CMTime?](./cmioextensionstreamproperties/frameduration-4rnl9.md)
  The duration of the frame.
- [var maxFrameDuration: CMTime?](./cmioextensionstreamproperties/maxframeduration-5qqg.md)
  The maximum duration of a frame.
- [activeFormatIndex](./cmioextensionstreamproperties/activeformatindex-8czm7.md)
  The index of the active format.
- [frameDuration](./cmioextensionstreamproperties/frameduration-lrfi.md)
  A dictionary representation of a frame duration.
- [maxFrameDuration](./cmioextensionstreamproperties/maxframeduration-8fo5t.md)
  The maximum duration of a frame.
### Managing Property State
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./cmioextensionstreamproperties/propertiesdictionary.md)
  A dictionary representation of the property state.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./cmioextensionstreamproperties/setpropertystate%28_,forproperty%29.md)
  Sets the state of the specified property.

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

### Streams
- [class CMIOExtensionStream](./cmioextensionstream.md)
  An object that represents a stream of media data.
- [protocol CMIOExtensionStreamSource](./cmioextensionstreamsource.md)
  A protocol for objects that act as stream sources.
- [class CMIOExtensionClient](./cmioextensionclient.md)
  An object that represents a client of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties)*