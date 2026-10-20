# registerFileRepresentation(forTypeIdentifier:fileOptions:visibility:loadHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func registerFileRepresentation(forTypeIdentifier typeIdentifier: String, fileOptions: NSItemProviderFileOptions = [], visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable (URL?, Bool, (any Error)?) -> Void) -> Progress?)
```

```objc
- (void) registerFileRepresentationForTypeIdentifier:(NSString *) typeIdentifier fileOptions:(NSItemProviderFileOptions) fileOptions visibility:(NSItemProviderRepresentationVisibility) visibility loadHandler:(NSProgress * (^)(void (^completionHandler)(NSURL *url, BOOL coordinated, NSError *error))) loadHandler;
```

#### Discussion

If a destination app must access the represented file using a file coordinator, set the `coordinated` parameter in the load handler block to [`true`](../../Swift/true.md).

To offer a representation backed by a file provider, return an [`NSURL`](../nsurl.md) object that points to your app’s file provider’s container. The file provider extension is then invoked to retrieve the file when requested.

To offer a representation backed by a file to open in place, set the fileOptions parameter to a value of [`openInPlace`](../nsitemproviderfileoptions/openinplace.md); in addition, return an [`NSURL`](../nsurl.md) object that points to your app’s file provider’s container. Open-in-place support requires that the file provider is visible in the Files app.

## See Also

### Registering files
- [func registerFileRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, openInPlace: Bool, loadHandler: ((URL?, Bool, (any Error)?) -> Void) -> Progress?)](./registerfilerepresentation%28for,visibility,openinplace,loadhandler%29.md)
  Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentation(fortypeidentifier:fileoptions:visibility:loadhandler:))*