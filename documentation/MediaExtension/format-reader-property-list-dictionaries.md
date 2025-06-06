# Format reader property list dictionaries

**Framework**: MediaExtension

Include property list dictionaries to describe a format reader and register the formats it supports.

#### Overview

An `ExtensionKit` format reader needs to include one required dictionary and can also include an optional dictionary in its `Info.plist` file:

1. `EXAppExtensionAttributes`: A required dictionary that describes the format reader and contains the following keys and values:

- [`kMEFormatReaderClassImplementationIDKey`](kmeformatreaderclassimplementationidkey.md): The identifier for the format reader. Format similarly to the bundle identifier.
- `EXExtensionPointIdentifier`: The extension point name for format readers. Set to the value for [`kMEFormatReaderExtensionPointName`](kmeformatreaderextensionpointname.md).
- `EXPrincipalClass`: The name of the format reader factory class that conforms to the [`MEFormatReaderExtension`](meformatreaderextension.md) protocol.
- [`kMEFormatReaderFileNameExtensionArrayKey`](kmeformatreaderfilenameextensionarraykey.md): An array of strings that specify the file name extensions that the format reader supports.
- [`kMEFormatReaderUTTypeArrayKey`](kmeformatreaderuttypearraykey.md): A key to the array of Uniform Type Identifiers that the format reader supports.
- [`kMEFormatReaderObjectNameKey`](kmeformatreaderobjectnamekey.md): A user-readable string that describes the format reader.

1. [`UTExportedTypeDeclarations`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations): An optional dictionary that registers the formats from the [`kMEFormatReaderUTTypeArrayKey`](kmeformatreaderuttypearraykey.md) array that the format reader supports, so the system can recognize those media files and open them in the appropriate app. It contains the following keys and values:

- [`UTTypeDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations/UTTypeDescription): A user-readable string that specifies the media kind, which Finder displays.
- [`UTTypeConformsTo`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations/UTTypeConformsTo): An array of `UTType` identifiers, with the first entry set to `com.apple.mediaextension-content`. This type also conforms to higher level abstract types such as `public.movie` and `public.audiovisual-content`. This array can include additional types as needed.
- [`UTTypeIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations/UTTypeIdentifier): This value needs to match the value for `kMEFormatReaderUTTypeArrayKey` in the `EXAppExtensionAttributes` dictionary.
- [`UTTypeTagSpecification`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations/UTTypeTagSpecification), `public.filename-extension` key: This value needs to match the value for [`kMEFormatReaderFileNameExtensionArrayKey`](kmeformatreaderfilenameextensionarraykey.md) in the `EXAppExtensionAttributes` dictionary.
- `public.mime-type`: This is an optional key to a MIME type that corresponds to the format.

For general information on how to make a `UTExportedTypeDeclarations` dictionary, see [`UTExportedTypeDeclarations`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UTExportedTypeDeclarations).

## Topics

### Property list keys
- [var kMEFormatReaderClassImplementationIDKey: String](kmeformatreaderclassimplementationidkey.md)
  The unique identifier for the format reader.
- [var kMEFormatReaderExtensionPointName: String](kmeformatreaderextensionpointname.md)
  A key to the extension point name for format readers.
- [var kMEFormatReaderFileNameExtensionArrayKey: String](kmeformatreaderfilenameextensionarraykey.md)
  A key to the array of file extensions that the format reader plug-in supports.
- [var kMEFormatReaderUTTypeArrayKey: String](kmeformatreaderuttypearraykey.md)
  A key to the array of Uniform Type Identifiers that the format reader supports.
- [var kMEFormatReaderObjectNameKey: String](kmeformatreaderobjectnamekey.md)
  A user-readable string describing the format reader.

## See Also

- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/format-reader-property-list-dictionaries)*