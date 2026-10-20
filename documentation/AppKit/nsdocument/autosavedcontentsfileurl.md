# autosavedContentsFileURL

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The location of the most recently autosaved document contents.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var autosavedContentsFileURL: URL? { get set }
```

```objc
@property (copy, nullable) NSURL * autosavedContentsFileURL;
```

#### Discussion

Use this property to specify the location where you want the document to store autosave files. The URL you specify should specify an absolute path, not a relative path.

## See Also

### Configuring the Autosave Behavior
- [class var autosavesInPlace: Bool](./autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var autosavesDrafts: Bool](./autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [class var preservesVersions: Bool](./preservesversions.md)
  A Boolean value that indicates whether the document subclass supports version management.
- [var autosavingFileType: String?](./autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](./autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosavedcontentsfileurl)*