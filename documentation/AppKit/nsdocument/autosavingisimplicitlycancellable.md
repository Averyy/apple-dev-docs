# autosavingIsImplicitlyCancellable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can cancel an in-progress autosave operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var autosavingIsImplicitlyCancellable: Bool { get }
```

```objc
@property (readonly) BOOL autosavingIsImplicitlyCancellable;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if autosaving is in progress but nothing bad would happen if it were cancelled. For example, when periodic autosaving is being done only for crash protection, which doesn’t need to be done all of the time, this property is set to [`true`](../../Swift/true.md). When autosaving is being done because the document is being closed, the property is set to [`false`](../../Swift/false.md).

When the value is [`true`](../../Swift/true.md), your document-writing code can invoke [`unblockUserInteraction()`](./unblockuserinteraction%28%29.md) after recording the fact that changes to the document model made by the user should first cancel the rest of the writing. Your code that makes changes to the document model then must always do that cancellation first. If your writing code is implicitly cancelled in this way, it should set the [`NSError`](../../Foundation/nserror.md) object passed by reference to the writing method to [`NSUserCancelledError`](../../Foundation/nsusercancellederror-swift.var.md) in [`NSCocoaErrorDomain`](../../Foundation/nscocoaerrordomain.md).

## See Also

### Configuring the Autosave Behavior
- [class var autosavesInPlace: Bool](./autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var autosavesDrafts: Bool](./autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](./preservesversions.md)
  A Boolean value that indicates whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](./autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](./autosavingfiletype.md)
  The document type to use for an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavingisimplicitlycancellable)*