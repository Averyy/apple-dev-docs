# loadObject(ofClass:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads an object of a specified class to an item provider, returning a progress object.

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
func loadObject(ofClass aClass: any NSItemProviderReading.Type, completionHandler: @escaping @Sendable ((any NSItemProviderReading)?, (any Error)?) -> Void) -> Progress
```

```objc
- (NSProgress *) loadObjectOfClass:(Class<NSItemProviderReading> *) aClass completionHandler:(void (^)(id<NSItemProviderReading>object, NSError *error)) completionHandler;
```

## See Also

### Loading the provider’s contents
- [func loadItem(forTypeIdentifier: String, options: [AnyHashable : Any]?, completionHandler: NSItemProvider.CompletionHandler?)](./loaditem%28fortypeidentifier,options,completionhandler%29.md)
  Loads the item’s data and coerces it to the specified type.
- [func loadDataRepresentation(forTypeIdentifier: String, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](./loaddatarepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [func loadDataRepresentation(for: UTType, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](./loaddatarepresentation%28for,completionhandler%29.md)
  Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [func loadFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, (any Error)?) -> Void) -> Progress](./loadfilerepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [func loadFileRepresentation(for: UTType, openInPlace: Bool, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](./loadfilerepresentation%28for,openinplace,completionhandler%29.md)
  Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [func loadInPlaceFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](./loadinplacefilerepresentation%28fortypeidentifier,completionhandler%29.md)
  Asynchronously opens a file in place, if possible, returning a progress object.
- [func loadObject<T>(ofClass: T.Type, completionHandler: (T?, (any Error)?) -> Void) -> Progress](./loadobject%28ofclass,completionhandler%29-6pysm.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [func loadTransferable<T>(type: T.Type, completionHandler: (Result<T, any Error>) -> Void) -> Progress](./loadtransferable%28type,completionhandler%29.md)
  Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/loadobject(ofclass:completionhandler:)-8ak5d)*