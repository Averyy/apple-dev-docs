# CMFormatDescription.Extensions

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A type that describes format description extensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Extensions
```

## Topics

### Creating Extensions
- [init()](./extensions-swift.struct/init%28%29.md)
  Creates an empty `Extensions` structure.
- [init(base: [CFString : CFPropertyList]?)](./extensions-swift.struct/init%28base%29.md)
  Creates an `Extensions` structure with existing values.
### Finding Extension Elements
- [subscript(CFString) -> CFPropertyList?](./extensions-swift.struct/subscript%28_%29-1c6vg.md)
- [subscript(CMFormatDescription.Extensions.Key) -> CMFormatDescription.Extensions.Value?](./extensions-swift.struct/subscript%28_%29-80zh8.md)
### Constants
- [CMFormatDescription.Extensions.Key](./extensions-swift.struct/key.md)
- [CMFormatDescription.Extensions.Value](./extensions-swift.struct/value.md)

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Constants
- [static var extensionKeysCommonWithImageBuffers: [CMFormatDescription.Extensions.Key]](./extensionkeyscommonwithimagebuffers.md)
  A constant that represents keys you use with video format description extensions and image buffers.
- [static var typeID: CFTypeID](./typeid.md)
  A type identifier that corresponds to a description object.
- [CMFormatDescription.MediaType](./mediatype-swift.struct.md)
  A type that describes format description media.
- [CMFormatDescription.MediaSubType](./mediasubtype-swift.struct.md)
  A type that describes format description media subtypes.
- [CMFormatDescription.TimeCode](./timecode.md)
  A type that describes format description time codes.
- [CMFormatDescription.EqualityMask](./equalitymask.md)
  A type that describes format description equality masks.
- [CMFormatDescription.ParameterSetCollection](./parametersetcollection.md)
  Collection of parameter sets in a video format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct)*