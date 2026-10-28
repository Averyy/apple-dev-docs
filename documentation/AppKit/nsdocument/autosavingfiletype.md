# autosavingFileType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The document type to use for an autosave operation.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var autosavingFileType: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * autosavingFileType;
```

## Discussion

This properties contains a string that identifies the document type for autosave files. The default implementation just returns the value provided by the [`fileType`](./filetype.md) property. You can override this property and return `nil` to completely disable autosaving of individual documents (because the [`NSDocumentController`](../nsdocumentcontroller.md) object does not call the  [`autosave(withDelegate:didAutosave:contextInfo:)`](./autosave%28withdelegate,didautosave,contextinfo%29.md) method of a document that has no autosaving file type). You can also override it if your app defines a document type that is specifically designed for autosaving, for example, one that efficiently represents document content changes instead of complete document contents.

Overriding this property can result in incorrect behavior during reopening of autosaved documents. The `NSDocument` method [`init(for:withContentsOf:ofType:)`](./init%28for,withcontentsof,oftype%29.md), which is invoked during reopening of autosaved documents after a crash, takes two URLs, but only the type name of the autosaved contents file. The default implementation updates the [`fileType`](./filetype.md) property with that type name, but that may not be the right thing to do if this property contains something other than [`fileType`](./filetype.md) during document autosaving. If you override `autosavingFileType`, you probably need to override [`init(for:withContentsOf:ofType:)`](./init%28for,withcontentsof,oftype%29.md) too, and make the override update [`fileType`](./filetype.md) with the type of the actual document file, after invoking `super`. See TextEdit’s `Document` class for an example of how to do this.

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
- [var autosavingIsImplicitlyCancellable: Bool](./autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavingfiletype)*