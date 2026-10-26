# CMIOExtensionStreamFormat

**Framework**: Core Media I/O  
**Kind**: class  
**Role**: Class

An object that describes the format of a media stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStreamFormat
```

```objc
@interface CMIOExtensionStreamFormat : NSObject
```

## Topics

### Creating a Stream Format
- [convenience init(formatDescription: CMFormatDescription, maxFrameDuration: CMTime, minFrameDuration: CMTime, validFrameDurations: [CMTime]?)](./cmioextensionstreamformat/init%28formatdescription,maxframeduration,minframeduration,validframedurations%29.md)
  Creates a stream format with a format description and frame durations.
- [+ streamFormatWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:](./cmioextensionstreamformat/streamformatwithformatdescription_maxframeduration_minframeduration_validframedurations_.md)
  Returns a new stream format with a format description and frame durations.
- [- initWithFormatDescription:maxFrameDuration:minFrameDuration:validFrameDurations:](./cmioextensionstreamformat/initwithformatdescription_maxframeduration_minframeduration_validframedurations_.md)
  Creates a stream format with a format description and frame durations.
### Configuring Frame Durations
- [var minFrameDuration: CMTime](./cmioextensionstreamformat/minframeduration.md)
  The minimum frame duration a stream supports.
- [var maxFrameDuration: CMTime](./cmioextensionstreamformat/maxframeduration.md)
  The maximum duration a stream supports.
- [var validFrameDurations: [CMTime]?](./cmioextensionstreamformat/validframedurations-707st.md)
  An array of frame durations the stream supports.
- [validFrameDurations](./cmioextensionstreamformat/validframedurations-4rbay.md)
  An array of frame durations the stream supports.
### Accessing the Format Description
- [var formatDescription: CMFormatDescription](./cmioextensionstreamformat/formatdescription.md)
  A description of the format of the stream’s media samples.
### Initializers
- [init?(coder: NSCoder)](./cmioextensionstreamformat/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Accessing the Source Format
- [var formats: [CMIOExtensionStreamFormat]](./cmioextensionstreamsource/formats.md)
  An array of formats that a stream supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat)*