# CMFormatDescription.Extensions

**Framework**: Core Media  
**Kind**: struct

A type that describes format description extensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
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
- [init()](cmformatdescription/extensions-swift.struct/init.md)
  Creates an empty `Extensions` structure.
- [init(base: [CFString : CFPropertyList]?)](cmformatdescription/extensions-swift.struct/init(base:).md)
  Creates an `Extensions` structure with existing values.
### Finding Extension Elements
- [subscript(CFString) -> CFPropertyList?](cmformatdescription/extensions-swift.struct/subscript(_:)-1c6vg.md)
- [subscript(CMFormatDescription.Extensions.Key) -> CMFormatDescription.Extensions.Value?](cmformatdescription/extensions-swift.struct/subscript(_:)-80zh8.md)
### Constants
- [CMFormatDescription.Extensions.Key](cmformatdescription/extensions-swift.struct/key.md)
- [CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [static var extensionKeysCommonWithImageBuffers: [CMFormatDescription.Extensions.Key]](cmformatdescription/extensionkeyscommonwithimagebuffers.md)
  A constant that represents keys you use with video format description extensions and image buffers.
- [static var typeID: CFTypeID](cmformatdescription/typeid.md)
  A type identifier that corresponds to a description object.
- [CMFormatDescription.MediaType](cmformatdescription/mediatype-swift.struct.md)
  A type that describes format description media.
- [CMFormatDescription.MediaSubType](cmformatdescription/mediasubtype-swift.struct.md)
  A type that describes format description media subtypes.
- [CMFormatDescription.TimeCode](cmformatdescription/timecode.md)
  A type that describes format description time codes.
- [CMFormatDescription.EqualityMask](cmformatdescription/equalitymask.md)
  A type that describes format description equality masks.
- [CMFormatDescription.ParameterSetCollection](cmformatdescription/parametersetcollection.md)
  Collection of parameter sets in a video format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct)*