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
### Initializers
- [init?(coder: NSCoder)](cmioextensionstreamformat/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [var formats: [CMIOExtensionStreamFormat]](cmioextensionstreamsource/formats.md)
  An array of formats that a stream supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamformat)*