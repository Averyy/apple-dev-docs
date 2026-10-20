# PropertyListSerialization.PropertyListFormat

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants are used to specify a property list serialization format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum PropertyListFormat
```

```c
enum NSPropertyListFormat : NSUInteger;
```

## Topics

### Constants
- [PropertyListSerialization.PropertyListFormat.openStep](./propertylistformat/openstep.md)
  Specifies the ASCII property list format inherited from the OpenStep APIs.
- [PropertyListSerialization.PropertyListFormat.xml](./propertylistformat/xml.md)
  Specifies the XML property list format.
- [PropertyListSerialization.PropertyListFormat.binary](./propertylistformat/binary.md)
  Specifies the binary property list format.
### Initializers
- [init?(rawValue: UInt)](./propertylistformat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [PropertyListSerialization.MutabilityOptions](./mutabilityoptions.md)
  These constants specify mutability options in property lists.
- [PropertyListSerialization.ReadOptions](./readoptions.md)
  The only read options supported are described in [`PropertyListSerialization.MutabilityOptions`](./mutabilityoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat)*