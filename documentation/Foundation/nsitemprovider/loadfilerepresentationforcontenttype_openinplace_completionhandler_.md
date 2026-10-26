# loadFileRepresentationForContentType:openInPlace:completionHandler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously copies the content type data into a generic data object with the specified parameters.

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
- (NSProgress *) loadFileRepresentationForContentType:(UTType *) contentType openInPlace:(BOOL) openInPlace completionHandler:(void (^)(NSURL *URL, BOOL openInPlace, NSError *error)) completionHandler;
```

## See Also

### Loading the provider’s contents
- [func loadItem(forTypeIdentifier: String, options: [AnyHashable : Any]?, completionHandler: NSItemProvider.CompletionHandler?)](./loaditem%28fortypeidentifier,options,completionhandler%29.md)
  Loads the item’s data and coerces it to the specified type.
- [func loadDataRepresentation(forTypeIdentifier: String, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](./loaddatarepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [- loadDataRepresentationForContentType:completionHandler:](./loaddatarepresentationforcontenttype_completionhandler_.md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [func loadFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, (any Error)?) -> Void) -> Progress](./loadfilerepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [func loadInPlaceFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](./loadinplacefilerepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously opens a file in place, if possible, returning a progress object.
- [func loadObject(ofClass: any NSItemProviderReading.Type, completionHandler: ((any NSItemProviderReading)?, (any Error)?) -> Void) -> Progress](./loadobject%28ofclass,completionhandler%29-8ak5d.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadfilerepresentationforcontenttype:openinplace:completionhandler:)*