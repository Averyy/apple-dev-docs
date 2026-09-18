# Format reader entitlement

**Framework**: MediaExtension

Include an entitlement to indicate your extension is a MediaExtension format reader.

#### Overview

MediaExtension format readers must include a special entitlement key with a Boolean value set to `true`. To add the entitlement key in Xcode, follow these steps:

1. Select the build target for your format reader extension.
2. Go to the Signing & Capabilities tab.
3. Click + to add a new capability.
4. Choose Media Extension Format Reader from the list.

The entitlement key is `com.apple.developer.mediaextension.formatreader` and it must have a Boolean value set to `true`. Using this entitlement requires a developer provisioning profile.

## See Also

- [Supporting custom media formats and decoders](supporting-custom-media-formats-and-decoders.md)
  Extend the media formats the system can open by providing a format reader and a video decoder.
- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/format-reader-entitlement)*