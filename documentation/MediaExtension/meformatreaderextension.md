# MEFormatReaderExtension

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines a factory to create a new format reader with a byte source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MEFormatReaderExtension : NSObjectProtocol
```

#### Overview

Media Toolbox creates the `MEFormatReaderExtension` object and the [`MEByteSource`](mebytesource.md) object based on the media asset.

## Topics

### Creating a format reader
- [init()](meformatreaderextension/init.md)
  Creates a new format reader factory.
- [func formatReader(with: MEByteSource, options: MEFormatReaderInstantiationOptions?) throws -> any MEFormatReader](meformatreaderextension/formatreader(with:options:).md)
  Creates a new format reader with the byte source and options that you specify.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderextension)*