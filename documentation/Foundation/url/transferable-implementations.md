# Transferable Implementations

**Framework**: Foundation

## Topics

### Initializers
- [init(importing: URL, contentType: UTType?) async throws](url/init(importing:contenttype:)-3gggv.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from the given file.
- [init(importing: Data, contentType: UTType?) async throws](url/init(importing:contenttype:)-80jg2.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from given data.
### Instance Properties
- [var suggestedFilename: String?](url/suggestedfilename.md)
  A suggested filename of a `Transferable` value.
### Instance Methods
- [func export(to: URL, contentType: UTType?) async throws -> URL](url/export(to:contenttype:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to a provided destination directory.
- [func exported(as: UTType?) async throws -> Data](url/exported(as:).md)
  Using the type’s `Transferable` conformance implementation, exports a value as binary data.
- [func exportedContentTypes(TransferRepresentationVisibility) -> [UTType]](url/exportedcontenttypes(_:).md)
  Content types supported by a given value’s `Transferable` conformance for export (like drag or copy).
- [func importedContentTypes() -> [UTType]](url/importedcontenttypes.md)
  Content types supported by a given value’s `Transferable` conformance for import (like drop or paste).
- [func withExportedFile<Result>(contentType: UTType?, fileHandler: (URL) async throws -> Result) async throws -> Result](url/withexportedfile(contenttype:filehandler:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to disk and removes when not needed.
### Type Aliases
- [typealias Representation](url/representation.md)
  The data type for conformance with the Core Transferable framework.
### Type Properties
- [static var transferRepresentation: some TransferRepresentation](url/transferrepresentation.md)
  The representation for importing and exporting an item using Core Transferable.
### Type Methods
- [static func exportedContentTypes(visibility: TransferRepresentationVisibility) -> [UTType]](url/exportedcontenttypes(visibility:).md)
  The types that the instance of a `Transferable` is able to provide a representation for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/transferable-implementations)*