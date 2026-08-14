# MEFormatReaderInstantiationOptions

**Framework**: MediaExtension  
**Kind**: class

An object that contains options to pass to a format reader extension.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEFormatReaderInstantiationOptions
```

#### Overview

This object is mutable with options set through instance properties.

## Topics

### Inspecting format reader extension options
- [var allowIncrementalFragmentParsing: Bool](meformatreaderinstantiationoptions/allowincrementalfragmentparsing.md)
  Enables support for parsing additional fragments.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderinstantiationoptions)*