# autosavesDrafts

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document subclass supports autosaving of drafts.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
class var autosavesDrafts: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiving subclass of [`NSDocument`](nsdocument.md) supports autosaving of drafts; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The system expects that an [`NSDocument`](nsdocument.md) subclass that returns [`true`](https://developer.apple.com/documentation/Swift/true) from this property can properly handle save operations that use the [`NSDocument.SaveOperationType.autosaveAsOperation`](nsdocument/saveoperationtype/autosaveasoperation.md) save operation type.

The default implementation of this property returns [`true`](https://developer.apple.com/documentation/Swift/true). To opt out of autosaving in your [`NSDocument`](nsdocument.md) subclass, override this property to return [`false`](https://developer.apple.com/documentation/Swift/false).

AppKit invokes this property at various times. For example, when calling the [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) method with [`NSDocument.ChangeType.changeDone`](nsdocument/changetype/changedone.md), but without the [`NSDocument.ChangeType.changeDiscardable`](nsdocument/changetype/changediscardable.md) change type, `NSDocument` uses [`NSDocument.SaveOperationType.autosaveAsOperation`](nsdocument/saveoperationtype/autosaveasoperation.md) on the next autosave. The operation writes the document’s contents to a new file or file package, then changes the document’s current location to point to the new file or file package.

Don’t invoke this property to find out whether autosaving of a draft might occur.

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var preservesVersions: Bool](nsdocument/preservesversions.md)
  A Boolean value that indicates whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](nsdocument/autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](nsdocument/autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavesdrafts)*