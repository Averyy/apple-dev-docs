# preservesVersions

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document subclass supports version management.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class var preservesVersions: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiving subclass of [`NSDocument`](nsdocument.md) supports Versions; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The default implementation of this method returns `[self autosavesInPlace]`. You can override it and return [`false`](https://developer.apple.com/documentation/Swift/false) to declare that `NSDocument` should not preserve old document versions.

Returning [`false`](https://developer.apple.com/documentation/Swift/false) from this method disables version browsing and [`revertToSaved(_:)`](nsdocument/reverttosaved(_:).md), which rely on version preservation when autosaving in place. Returning [`true`](https://developer.apple.com/documentation/Swift/true) from this method when [`autosavesInPlace`](nsdocument/autosavesinplace.md) returns [`false`](https://developer.apple.com/documentation/Swift/false) will result in undefined behavior.

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var autosavesDrafts: Bool](nsdocument/autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](nsdocument/autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](nsdocument/autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preservesversions)*