# formatReader(with:options:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Creates a new format reader with the byte source and options that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func formatReader(with primaryByteSource: MEByteSource, options: MEFormatReaderInstantiationOptions?) throws -> any MEFormatReader
```

#### Return Value

A new format reader.

## Parameters

- `primaryByteSource`: The primary byte source for the format reader.
- `options`: The reader instantiation options.

## See Also

- [init()](meformatreaderextension/init.md)
  Creates a new format reader factory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderextension/formatreader(with:options:))*