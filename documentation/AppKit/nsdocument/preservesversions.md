# preservesVersions

**Framework**: AppKit  
**Kind**: property

Returns whether the document subclass supports version management.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class var preservesVersions: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiving subclass of [`NSDocument`](nsdocument.md) supports Versions; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The default implementation of this method returns `[self autosavesInPlace]`. You can override it and return [`false`](https://developer.apple.com/documentation/swift/false) to declare that `NSDocument` should not preserve old document versions.

Returning [`false`](https://developer.apple.com/documentation/swift/false) from this method disables version browsing and [`revertToSaved(_:)`](nsdocument/reverttosaved(_:).md), which rely on version preservation when autosaving in place. Returning [`true`](https://developer.apple.com/documentation/swift/true) from this method when [`autosavesInPlace`](nsdocument/autosavesinplace.md) returns [`false`](https://developer.apple.com/documentation/swift/false) will result in undefined behavior.

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  Returns whether the receiver supports autosaving in place.
- [class var autosavesDrafts: Bool](nsdocument/autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](nsdocument/autosavingfiletype.md)
  Returns the document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](nsdocument/autosavingisimplicitlycancellable.md)
  Returns a Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preservesversions)*