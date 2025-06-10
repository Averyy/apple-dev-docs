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

### Comparing Extensions
- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](cmformatdescription/==(_:_:).md)
  Equality is derived from
### Creating Extensions
- [init()](cmformatdescription/extensions-swift.struct/init.md)
- [init(base: [CFString : CFPropertyList]?)](cmformatdescription/extensions-swift.struct/init(base:).md)
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
  A type that describes format description parameter sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct)*