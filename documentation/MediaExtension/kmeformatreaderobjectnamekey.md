# kMEFormatReaderObjectNameKey

**Framework**: MediaExtension  
**Kind**: var

A user-readable string describing the format reader.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEFormatReaderObjectNameKey: String { get }
```

#### Discussion

This string is used internally for uniquely identifying format readers and possibly for debug logging but is typically not visible to users.

## See Also

- [var kMEFormatReaderClassImplementationIDKey: String](kmeformatreaderclassimplementationidkey.md)
  The unique identifier for the format reader.
- [var kMEFormatReaderExtensionPointName: String](kmeformatreaderextensionpointname.md)
  A key to the extension point name for format readers.
- [var kMEFormatReaderFileNameExtensionArrayKey: String](kmeformatreaderfilenameextensionarraykey.md)
  A key to the array of file extensions that the format reader plug-in supports.
- [var kMEFormatReaderUTTypeArrayKey: String](kmeformatreaderuttypearraykey.md)
  A key to the array of Uniform Type Identifiers that the format reader supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmeformatreaderobjectnamekey)*