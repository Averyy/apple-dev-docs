# preservesVersions

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the document subclass supports version management.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var preservesVersions: Bool { get }
```

```objc
@property (class, readonly) BOOL preservesVersions;
```

## Return Value

[`true`](../../Swift/true.md) if the receiving subclass of [`NSDocument`](../nsdocument.md) supports Versions; otherwise [`false`](../../Swift/false.md).

## Discussion

The default implementation of this method returns `[self autosavesInPlace]`. You can override it and return [`false`](../../Swift/false.md) to declare that `NSDocument` should not preserve old document versions.

Returning [`false`](../../Swift/false.md) from this method disables version browsing and [`revertToSaved(_:)`](./reverttosaved%28_%29.md), which rely on version preservation when autosaving in place. Returning [`true`](../../Swift/true.md) from this method when [`autosavesInPlace`](./autosavesinplace.md) returns [`false`](../../Swift/false.md) will result in undefined behavior.

## See Also

### Configuring the Autosave Behavior
- [class var autosavesInPlace: Bool](./autosavesinplace.md)
  A Boolean value that indicates whether the document subclass supports autosaving in place.
- [class var autosavesDrafts: Bool](./autosavesdrafts.md)
  A Boolean value that indicates whether the document subclass supports autosaving of drafts.
- [var autosavedContentsFileURL: URL?](./autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [var autosavingFileType: String?](./autosavingfiletype.md)
  The document type to use for an autosave operation.
- [var autosavingIsImplicitlyCancellable: Bool](./autosavingisimplicitlycancellable.md)
  A Boolean value that indicates whether you can cancel an in-progress autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/preservesversions)*