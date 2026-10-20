# autosavesDrafts

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the document subclass supports autosaving of drafts.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class var autosavesDrafts: Bool { get }
```

```objc
@property (class, readonly) BOOL autosavesDrafts;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiving subclass of [`NSDocument`](../nsdocument.md) supports autosaving of drafts; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The system expects that an [`NSDocument`](../nsdocument.md) subclass that returns [`true`](../../Swift/true.md) from this property can properly handle save operations that use the [`NSDocument.SaveOperationType.autosaveAsOperation`](./saveoperationtype/autosaveasoperation.md) save operation type.

The default implementation of this property returns [`true`](../../Swift/true.md). To opt out of autosaving in your [`NSDocument`](../nsdocument.md) subclass, override this property to return [`false`](../../Swift/false.md).

AppKit invokes this property at various times. For example, when calling the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method with [`NSDocument.ChangeType.changeDone`](./changetype/changedone.md), but without the [`NSDocument.ChangeType.changeDiscardable`](./changetype/changediscardable.md) change type, `NSDocument` uses [`NSDocument.SaveOperationType.autosaveAsOperation`](./saveoperationtype/autosaveasoperation.md) on the next autosave. The operation writes the document’s contents to a new file or file package, then changes the document’s current location to point to the new file or file package.

Don’t invoke this property to find out whether autosaving of a draft might occur.

## See Also

### Configuring the Autosave Behavior
- [class var autosavesInPlace: Bool](./autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var preservesVersions: Bool](./preservesversions.md)
  A Boolean value that indicates whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](./autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](./autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](./autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavesdrafts)*