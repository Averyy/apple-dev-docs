# registerItem(forTypeIdentifier:loadHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Lazily registers an item, according to the item provider type coercion policy.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use registerObjectOfClass:visibility:loadHandler: instead.

## Declaration

```swift
func registerItem(forTypeIdentifier typeIdentifier: String, loadHandler: @escaping NSItemProvider.LoadHandler)
```

```objc
- (void) registerItemForTypeIdentifier:(NSString *) typeIdentifier loadHandler:(NSItemProviderLoadHandler) loadHandler;
```

## Discussion

Use this method to register blocks that can take the item provider’s file or data object and convert it to a specific data format. Your `loadHandler` block is executed when a client passes the same `typeIdentifier` string to the [`loadItem(forTypeIdentifier:options:completionHandler:)`](./loaditem%28fortypeidentifier,options,completionhandler%29.md) method. In the implementation of your block, coerce the data to the specified type and call the provided completion handler. You must call the completion handler, either with the requested data or with an error.

Item providers know how to coerce known types of objects, such as images or strings. Use this method to register blocks to coerce your custom data types.

## Parameters

- `typeIdentifier`: A string that represents the desired UTI.
- `loadHandler`: A block capable of returning the data item as the specified type. For information about implementing this block, see [`NSItemProvider.LoadHandler`](./loadhandler.md).

## See Also

### Registering data
- [func registerDataRepresentation(forTypeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](./registerdatarepresentation%28fortypeidentifier,visibility,loadhandler%29.md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerDataRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](./registerdatarepresentation%28for,visibility,loadhandler%29.md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [- registerDataRepresentationForContentType:visibility:loadHandler:](./registerdatarepresentationforcontenttype_visibility_loadhandler_.md)
  Lazily registers an item, according to the item provider type coercion policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeritem(fortypeidentifier:loadhandler:))*