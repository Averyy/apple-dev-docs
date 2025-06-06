# Transferable Implementations

**Framework**: Swift

## Topics

### Initializers
- [init(importing: Data, contentType: UTType?) async throws](never/init(importing:contenttype:)-5harc.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from given data.
- [init(importing: URL, contentType: UTType?) async throws](never/init(importing:contenttype:)-7tfxk.md)
  Using the type’s `Transferable` conformance implementation, instantiates a value from the given file.
### Instance Properties
- [var suggestedFilename: String?](never/suggestedfilename.md)
  A suggested filename of a `Transferable` value.
### Instance Methods
- [func export(to: URL, contentType: UTType?) async throws -> URL](never/export(to:contenttype:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to a provided destination directory.
- [func exported(as: UTType?) async throws -> Data](never/exported(as:).md)
  Using the type’s `Transferable` conformance implementation, exports a value as binary data.
- [func exportedContentTypes(TransferRepresentationVisibility) -> [UTType]](never/exportedcontenttypes(_:).md)
  Content types supported by a given value’s `Transferable` conformance for export (like drag or copy).
- [func importedContentTypes() -> [UTType]](never/importedcontenttypes.md)
  Content types supported by a given value’s `Transferable` conformance for import (like drop or paste).
- [func withExportedFile<Result>(contentType: UTType?, fileHandler: (URL) async throws -> Result) async throws -> Result](never/withexportedfile(contenttype:filehandler:).md)
  Using the type’s `Transferable` conformance implementation, exports a value by writing it to disk and removes when not needed.
### Type Aliases
- [typealias Representation](never/representation.md)
  The type of the representation used to import and export the item.
### Type Properties
- [static var transferRepresentation: Never](never/transferrepresentation.md)
  The representation used to import and export the item.
### Type Methods
- [static func exportedContentTypes(visibility: TransferRepresentationVisibility) -> [UTType]](never/exportedcontenttypes(visibility:).md)
  The types that the instance of a `Transferable` is able to provide a representation for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/transferable-implementations)*