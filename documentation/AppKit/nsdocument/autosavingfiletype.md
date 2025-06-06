# autosavingFileType

**Framework**: AppKit  
**Kind**: property

Returns the document type to use for an autosave operation.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var autosavingFileType: String? { get }
```

#### Discussion

This properties contains a string that identifies the document type for autosave files. The default implementation just returns the value provided by the [`fileType`](nsdocument/filetype.md) property. You can override this property and return `nil` to completely disable autosaving of individual documents (because the [`NSDocumentController`](nsdocumentcontroller.md) object does not call the  [`autosave(withDelegate:didAutosave:contextInfo:)`](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md) method of a document that has no autosaving file type). You can also override it if your app defines a document type that is specifically designed for autosaving, for example, one that efficiently represents document content changes instead of complete document contents.

Overriding this property can result in incorrect behavior during reopening of autosaved documents. The `NSDocument` method [`init(for:withContentsOf:ofType:)`](nsdocument/init(for:withcontentsof:oftype:).md), which is invoked during reopening of autosaved documents after a crash, takes two URLs, but only the type name of the autosaved contents file. The default implementation updates the [`fileType`](nsdocument/filetype.md) property with that type name, but that may not be the right thing to do if this property contains something other than [`fileType`](nsdocument/filetype.md) during document autosaving. If you override `autosavingFileType`, you probably need to override [`init(for:withContentsOf:ofType:)`](nsdocument/init(for:withcontentsof:oftype:).md) too, and make the override update [`fileType`](nsdocument/filetype.md) with the type of the actual document file, after invoking `super`. See TextEdit’s `Document` class for an example of how to do this.

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  Returns whether the receiver supports autosaving in place.
- [class var autosavesDrafts: Bool](nsdocument/autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](nsdocument/preservesversions.md)
  Returns whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingIsImplicitlyCancellable: Bool](nsdocument/autosavingisimplicitlycancellable.md)
  Returns a Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavingfiletype)*