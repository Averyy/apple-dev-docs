# Transferable Implementations

**Framework**: Foundation

## Topics

### Initializers
- [init(importing: URL, contentType: UTType?) async throws](attributedstring/init(importing:contenttype:)-4x92c.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from the given file.
- [init(importing: Data, contentType: UTType?) async throws](attributedstring/init(importing:contenttype:)-8v6d.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from given data.
### Instance Properties
- [var suggestedFilename: String?](attributedstring/suggestedfilename.md)
  A suggested filename of a `Transferable` value.
### Instance Methods
- [func export(to: URL, contentType: UTType?) async throws -> URL](attributedstring/export(to:contenttype:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to a provided destination directory.
- [func exported(as: UTType?) async throws -> Data](attributedstring/exported(as:).md)
  Using the type’s `Transferable` conformance implementation, exports a value as binary data.
- [func exportedContentTypes(TransferRepresentationVisibility) -> [UTType]](attributedstring/exportedcontenttypes(_:).md)
  Content types supported by a given value’s `Transferable` conformance for export (like drag or copy).
- [func importedContentTypes() -> [UTType]](attributedstring/importedcontenttypes.md)
  Content types supported by a given value’s `Transferable` conformance for import (like drop or paste).
- [func withExportedFile<Result>(contentType: UTType?, fileHandler: (URL) async throws -> Result) async throws -> Result](attributedstring/withexportedfile(contenttype:filehandler:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to disk and removes when not needed.
### Type Aliases
- [AttributedString.Representation](attributedstring/representation.md)
### Type Properties
- [static var transferRepresentation: some TransferRepresentation](attributedstring/transferrepresentation.md)
### Type Methods
- [static func exportedContentTypes(visibility: TransferRepresentationVisibility) -> [UTType]](attributedstring/exportedcontenttypes(visibility:).md)
  The types that the instance of a `Transferable` is able to provide a representation for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transferable-implementations)*