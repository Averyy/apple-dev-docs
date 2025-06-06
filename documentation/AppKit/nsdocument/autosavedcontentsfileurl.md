# autosavedContentsFileURL

**Framework**: AppKit  
**Kind**: property

The location of the most recently autosaved document contents.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var autosavedContentsFileURL: URL? { get set }
```

#### Discussion

Use this property to specify the location where you want the document to store autosave files. The URL you specify should specify an absolute path, not a relative path.

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  Returns whether the receiver supports autosaving in place.
- [class var autosavesDrafts: Bool](nsdocument/autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](nsdocument/preservesversions.md)
  Returns whether the document subclass supports version management.
- [var autosavingFileType: String?](nsdocument/autosavingfiletype.md)
  Returns the document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](nsdocument/autosavingisimplicitlycancellable.md)
  Returns a Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavedcontentsfileurl)*