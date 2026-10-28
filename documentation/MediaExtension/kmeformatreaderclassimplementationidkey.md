# kMEFormatReaderClassImplementationIDKey

**Framework**: MediaExtension  
**Kind**: var  
**Role**: Global Variable

The unique identifier for the format reader.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var kMEFormatReaderClassImplementationIDKey: String { get }
```

```c
#define kMEFormatReaderClassImplementationIDKey
```

## Discussion

Format the string similar to the bundle identifier of the format reader. Start with the reverse domain identifier of your developer account, followed by `.formatreader.` and the name of the media format. If you plan to create multiple variants of the same media format, include an additional component to make each format reader identifier unique; for example `com.mycompany.formatreader.mymediaformat.formatvariant`.

## See Also

### Property list keys
- [var kMEFormatReaderExtensionPointName: String](./kmeformatreaderextensionpointname.md)
  A key to the extension point name for format readers.
- [var kMEFormatReaderFileNameExtensionArrayKey: String](./kmeformatreaderfilenameextensionarraykey.md)
  A key to the array of file extensions that the format reader plug-in supports.
- [var kMEFormatReaderUTTypeArrayKey: String](./kmeformatreaderuttypearraykey.md)
  A key to the array of Uniform Type Identifiers that the format reader supports.
- [var kMEFormatReaderObjectNameKey: String](./kmeformatreaderobjectnamekey.md)
  A user-readable string describing the format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/kmeformatreaderclassimplementationidkey)*