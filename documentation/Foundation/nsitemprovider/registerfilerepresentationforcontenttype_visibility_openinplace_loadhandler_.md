# registerFileRepresentationForContentType:visibility:openInPlace:loadHandler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) registerFileRepresentationForContentType:(UTType *) contentType visibility:(NSItemProviderRepresentationVisibility) visibility openInPlace:(BOOL) openInPlace loadHandler:(NSProgress * (^)(void (^completionHandler)(NSURL *fileURL, BOOL coordinated, NSError *error))) loadHandler;
```

## See Also

### Registering files
- [func registerFileRepresentation(forTypeIdentifier: String, fileOptions: NSItemProviderFileOptions, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((URL?, Bool, (any Error)?) -> Void) -> Progress?)](./registerfilerepresentation%28fortypeidentifier,fileoptions,visibility,loadhandler%29.md)
  Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerfilerepresentationforcontenttype:visibility:openinplace:loadhandler:)*