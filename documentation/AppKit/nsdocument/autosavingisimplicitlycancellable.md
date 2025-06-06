# autosavingIsImplicitlyCancellable

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value that indicates whether you can cancel an in-progress autosave operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var autosavingIsImplicitlyCancellable: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if autosaving is in progress but nothing bad would happen if it were cancelled. For example, when periodic autosaving is being done only for crash protection, which doesn’t need to be done all of the time, this property is set to [`true`](https://developer.apple.com/documentation/swift/true). When autosaving is being done because the document is being closed, the property is set to [`false`](https://developer.apple.com/documentation/swift/false).

When the value is [`true`](https://developer.apple.com/documentation/swift/true), your document-writing code can invoke [`unblockUserInteraction()`](nsdocument/unblockuserinteraction().md) after recording the fact that changes to the document model made by the user should first cancel the rest of the writing. Your code that makes changes to the document model then must always do that cancellation first. If your writing code is implicitly cancelled in this way, it should set the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object passed by reference to the writing method to [`NSUserCancelledError`](https://developer.apple.com/documentation/foundation/nsusercancellederror) in [`NSCocoaErrorDomain`](https://developer.apple.com/documentation/Foundation/NSCocoaErrorDomain).

## See Also

- [class var autosavesInPlace: Bool](nsdocument/autosavesinplace.md)
  Returns whether the receiver supports autosaving in place.
- [class var autosavesDrafts: Bool](nsdocument/autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](nsdocument/preservesversions.md)
  Returns whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](nsdocument/autosavingfiletype.md)
  Returns the document type to use for an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavingisimplicitlycancellable)*