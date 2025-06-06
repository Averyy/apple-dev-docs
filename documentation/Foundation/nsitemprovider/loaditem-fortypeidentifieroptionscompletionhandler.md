# loadItem(forTypeIdentifier:options:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Loads the item’s data and coerces it to the specified type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func loadItem(forTypeIdentifier typeIdentifier: String, options: [AnyHashable : Any]? = nil) async throws -> any NSSecureCoding
```

#### Discussion

Call this method when you want to retrieve the item provider’s data. If the item provider object is able to provide data in the requested type, it does so and asynchronously executes your `completionHandler` block with the results. The block may be executed on a background thread.

The type information for the first parameter of your `completionHandler` block should be set to the class of the expected type. For example, when requesting text data, you might set the type of the first parameter to [`NSString`](nsstring.md) or [`NSAttributedString`](nsattributedstring.md). An item provider can perform simple type conversions of the data to the class you specify, such as from [`NSURL`](nsurl.md) to [`NSData`](nsdata.md) or [`FileWrapper`](filewrapper.md), or from [`NSData`](nsdata.md) to [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) (in iOS) or [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) (in macOS). If the data could not be retrieved or coerced to the specified class, an error is passed to the completion block’s.

## Parameters

- `typeIdentifier`: A string that represents the desired UTI.
- `options`: A dictionary of keys and values that provide information about the item, such as the size of an image. (See   for a key you can use.)
- `completionHandler`: A completion handler block to execute with the results. For information about the format of this block, see  .

## See Also

- [func loadDataRepresentation(forTypeIdentifier: String, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [func loadDataRepresentation(for: UTType, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(for:completionhandler:).md)
  Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [func loadFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadfilerepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:))*