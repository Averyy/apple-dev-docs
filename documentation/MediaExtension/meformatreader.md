# MEFormatReader

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines the requirements for a format reader, which represents a single media asset.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MEFormatReader : NSObjectProtocol
```

#### Overview

This protocol provides an interface for the Media Toolbox to interact with extension plug-in format readers, which provide information about media assets. `MEFormatReader` objects are always instantiated by the Media Toolbox.

> **Note**:  Developers who wish to build MediaExtension format readers using this API need to include a [`Format reader entitlement`](format-reader-entitlement.md), provisioning profile, and specialized dictionary in their Info.plist file when building their extensions. For more information, see [`Entitlements`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements), [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-provisioning-profiles/create-a-development-provisioning-profile), and [`Format reader property list dictionaries`](format-reader-property-list-dictionaries.md).

To create an `MEFormatReader` object, Media Toolbox first creates a primary [`MEByteSource`](mebytesource.md) object from a source media asset. It then creates an [`MEFormatReaderExtension`](meformatreaderextension.md) object and calls its [`formatReader(with:options:)`](meformatreaderextension/formatreader(with:options:).md) method.

Once a user installs and runs the host app, embedded MediaExtension format reader extensions become available to any app on the user’s system that opts in to using them by calling [`MTRegisterProfessionalVideoWorkflowFormatReaders()`](https://developer.apple.com/documentation/MediaToolbox/MTRegisterProfessionalVideoWorkflowFormatReaders()).

> ❗ **Important**:  `MEFormatReader` objects run in a sandboxed process with restricted access to the filesystem, network, and other kernel resources.

## Topics

### Reading and parsing media assets
- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](meformatreader/loadfileinfo(completionhandler:).md)
  Loads the file info object with the properties of the media asset.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](meformatreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset.
- [func loadTrackReaders(completionHandler: ([any METrackReader]?, (any Error)?) -> Void)](meformatreader/loadtrackreaders(completionhandler:).md)
  Loads the array of track readers that represent the tracks in the media asset.
- [func parseAdditionalFragments(completionHandler: (MEFormatReaderParseAdditionalFragmentsStatus, (any Error)?) -> Void)](meformatreader/parseadditionalfragments(completionhandler:).md)
  Incorporates additional fragments that the file received after the last time the format reader parsed it.
- [struct MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus.md)
  Informational status flags that the format reader returns after parsing additional fragments.
### Extension requirements
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreader)*