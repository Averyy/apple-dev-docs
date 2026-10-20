# MEFormatReaderInstantiationOptions

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that contains options to pass to a format reader extension.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEFormatReaderInstantiationOptions
```

```objc
@interface MEFormatReaderInstantiationOptions : NSObject
```

#### Overview

This object is mutable with options set through instance properties.

## Topics

### Inspecting format reader extension options
- [var allowIncrementalFragmentParsing: Bool](./meformatreaderinstantiationoptions/allowincrementalfragmentparsing.md)
  Enables support for parsing additional fragments.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Format readers
- [Supporting custom media formats and decoders](./supporting-custom-media-formats-and-decoders.md)
  Extend the media formats the system can open by providing a format reader and a video decoder.
- [protocol MEFormatReader](./meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](./meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFileInfo](./mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](./format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](./format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderinstantiationoptions)*