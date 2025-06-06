# CFPropertyListFormat

**Framework**: Core Foundation  
**Kind**: enum

Specifies the format of a property list.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFPropertyListFormat
```

## Topics

### Constants
- [CFPropertyListFormat.openStepFormat](cfpropertylistformat/openstepformat.md)
  OpenStep format (use of this format is discouraged).
- [CFPropertyListFormat.xmlFormat_v1_0](cfpropertylistformat/xmlformat_v1_0.md)
  XML format version 1.0.
- [CFPropertyListFormat.binaryFormat_v1_0](cfpropertylistformat/binaryformat_v1_0.md)
  Binary format version 1.0.
### Initializers
- [init?(rawValue: CFIndex)](cfpropertylistformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Property List Mutability Options](property_list_mutability_options.md)
  Option flags that determine the degree of mutability of newly created property lists.
- [Reading and Writing Error Codes](1429999-reading-and-writing-error-codes.md)
  Error codes for property list reading and writing functions such as [`CFPropertyListCreateWithData(_:_:_:_:_:)`](cfpropertylistcreatewithdata(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistformat)*