# loadFileRepresentation(forTypeIdentifier:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.

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
func loadFileRepresentation(forTypeIdentifier typeIdentifier: String, completionHandler: @escaping (URL?, (any Error)?) -> Void) -> Progress
```

#### Discussion

This method writes a copy of the file’s data to a temporary file, which the system deletes when the completion handler returns.

## See Also

- [func loadItem(forTypeIdentifier: String, options: [AnyHashable : Any]?, completionHandler: NSItemProvider.CompletionHandler?)](nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:).md)
  Loads the item’s data and coerces it to the specified type.
- [func loadDataRepresentation(forTypeIdentifier: String, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [func loadDataRepresentation(for: UTType, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(for:completionhandler:).md)
  Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [func loadFileRepresentation(for: UTType, openInPlace: Bool, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](nsitemprovider/loadfilerepresentation(for:openinplace:completionhandler:).md)
  Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [func loadInPlaceFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](nsitemprovider/loadinplacefilerepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously opens a file in place, if possible, returning a progress object.
- [func loadObject(ofClass: any NSItemProviderReading.Type, completionHandler: ((any NSItemProviderReading)?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadobject(ofclass:completionhandler:)-8ak5d.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [func loadObject<T>(ofClass: T.Type, completionHandler: (T?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadobject(ofclass:completionhandler:)-6pysm.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [func loadTransferable<T>(type: T.Type, completionHandler: (Result<T, any Error>) -> Void) -> Progress](nsitemprovider/loadtransferable(type:completionhandler:).md)
  Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadfilerepresentation(fortypeidentifier:completionhandler:))*