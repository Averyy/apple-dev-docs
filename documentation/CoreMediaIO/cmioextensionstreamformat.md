# CMIOExtensionStreamFormat

**Framework**: Core Media I/O  
**Kind**: class

An object that describes the format of a media stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionStreamFormat
```

## Topics

### Creating a Stream Format
- [convenience init(formatDescription: CMFormatDescription, maxFrameDuration: CMTime, minFrameDuration: CMTime, validFrameDurations: [CMTime]?)](cmioextensionstreamformat/init(formatdescription:maxframeduration:minframeduration:validframedurations:).md)
  Creates a stream format with a format description and frame durations.
### Configuring Frame Durations
- [var minFrameDuration: CMTime](cmioextensionstreamformat/minframeduration.md)
  The minimum frame duration a stream supports.
- [var maxFrameDuration: CMTime](cmioextensionstreamformat/maxframeduration.md)
  The maximum duration a stream supports.
- [var validFrameDurations: [CMTime]?](cmioextensionstreamformat/validframedurations-707st.md)
  An array of frame durations the stream supports.
### Accessing the Format Description
- [var formatDescription: CMFormatDescription](cmioextensionstreamformat/formatdescription.md)
  A description of the format of the stream’s media samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var formats: [CMIOExtensionStreamFormat]](cmioextensionstreamsource/formats.md)
  An array of formats that a stream supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat)*