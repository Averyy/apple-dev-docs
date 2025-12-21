# registerFileRepresentation(for:visibility:openInPlace:loadHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func registerFileRepresentation(for contentType: UTType, visibility: NSItemProviderRepresentationVisibility = .all, openInPlace: Bool = false, loadHandler: @escaping (@escaping (URL?, Bool, (any Error)?) -> Void) -> Progress?)
```

#### Discussion

If a destination app must access the represented file using a file coordinator, set the `coordinated` parameter in the load handler block to [`true`](https://developer.apple.com/documentation/Swift/true).

To offer a representation backed by a file provider, return an [`NSURL`](nsurl.md) object that points to your app’s file provider’s container. The file provider extension is then invoked to retrieve the file when requested.

To offer a representation backed by a file to open in place, set the fileOptions parameter to a value of [`openInPlace`](nsitemproviderfileoptions/openinplace.md); in addition, return an [`NSURL`](nsurl.md) object that points to your app’s file provider’s container. Open-in-place support requires that the file provider is visible in the Files app.

## See Also

- [func registerFileRepresentation(forTypeIdentifier: String, fileOptions: NSItemProviderFileOptions, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((URL?, Bool, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerfilerepresentation(fortypeidentifier:fileoptions:visibility:loadhandler:).md)
  Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentation(for:visibility:openinplace:loadhandler:))*