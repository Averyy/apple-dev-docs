# CVAttachmentKeyDefinition

**Framework**: Core Video  
**Kind**: struct

Associates a raw attachment key with a value type and preferred propagation mode.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct CVAttachmentKeyDefinition<ModePreference, Value> where ModePreference : CVAttachmentModePreference, Value : CVAttachmentValueRepresentable
```

## Topics

### Initializers
- [init(String)](cvattachmentkeydefinition/init(_:).md)
### Instance Properties
- [var rawValue: String](cvattachmentkeydefinition/rawvalue.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CVAttachmentAccess](cvattachmentaccess.md)
  Provides access to the attachments of a buffer.
- [struct CVAttachmentContainer](cvattachmentcontainer.md)
  Provides storage for buffer attachments independent of the buffer lifetime
- [struct CVAttachmentRawValue](cvattachmentrawvalue.md)
  A lightweight wrapper around raw attachment values.
- [struct CVAttachmentKeyDefinitionWithDefault](cvattachmentkeydefinitionwithdefault.md)
  Associates a raw attachment key with a default value and preferred propagation mode.
- [struct CVAttachmentCompositeKeyDefinition](cvattachmentcompositekeydefinition.md)
  Associates a set of raw attachment keys with a value type and preferred propagation mode.
- [enum CVAttachmentModePreferenceShouldPropagate](cvattachmentmodepreferenceshouldpropagate.md)
  Sets preferred mode for attachment to should propagate
- [enum CVAttachmentModePreferenceShouldNotPropagate](cvattachmentmodepreferenceshouldnotpropagate.md)
  Sets preferred mode for attachment to should not propagate


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentkeydefinition)*