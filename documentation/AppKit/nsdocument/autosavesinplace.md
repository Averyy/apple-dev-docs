# autosavesInPlace

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the document subclass supports autosaving in place.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
class var autosavesInPlace: Bool { get }
```

```objc
@property (class, readonly) BOOL autosavesInPlace;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver supports autosaving in place; [`false`](../../Swift/false.md) otherwise.

#### Discussion

The default implementation of this method returns [`false`](../../Swift/false.md). You can override it and return [`true`](../../Swift/true.md) to declare that your subclass of `NSDocument` can do autosaving in place. You should not invoke this method to find out whether autosaving in place is actually being done at any particular moment. You should instead use the [`NSDocument.SaveOperationType`](./saveoperationtype.md) parameter that the system passes to your overrides of save and write methods.

AppKit invokes this method at a variety of times, and not always on the main thread. For example, [`autosave(withImplicitCancellability:completionHandler:)`](./autosave%28withimplicitcancellability,completionhandler%29.md) invokes this method as part of determining whether the autosaving will be performed in place ([`NSDocument.SaveOperationType.autosaveInPlaceOperation`](./saveoperationtype/autosaveinplaceoperation.md)) or in a separate autosave directory ([`NSDocument.SaveOperationType.autosaveElsewhereOperation`](./saveoperationtype/autosaveelsewhereoperation.md)). As another example, the [`canClose(withDelegate:shouldClose:contextInfo:)`](./canclose%28withdelegate,shouldclose,contextinfo%29.md) method and the [`NSDocumentController`](../nsdocumentcontroller.md) machinery for handling unsaved changes at app termination time both invoke this method as part of determining whether alerts about unsaved changes should be presented to the user.

## See Also

### Configuring the Autosave Behavior
- [class var autosavesDrafts: Bool](./autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](./preservesversions.md)
  A Boolean value that indicates whether the document subclass supports version management.
- [var autosavedContentsFileURL: URL?](./autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](./autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](./autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavesinplace)*