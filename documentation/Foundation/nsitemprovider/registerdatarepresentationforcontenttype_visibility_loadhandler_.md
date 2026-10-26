# registerDataRepresentationForContentType:visibility:loadHandler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Lazily registers an item, according to the item provider type coercion policy.

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
- (void) registerDataRepresentationForContentType:(UTType *) contentType visibility:(NSItemProviderRepresentationVisibility) visibility loadHandler:(NSProgress * (^)(void (^completionHandler)(NSData *data, NSError *error))) loadHandler;
```

## Parameters

- `contentType`: A string that represents the desired UTI.
- `visibility`: The [`NSItemProviderRepresentationVisibility`](../nsitemproviderrepresentationvisibility.md) setting.
- `loadHandler`: A block capable of returning the data item as the specified type. For information about implementing this block, see [`NSItemProvider.LoadHandler`](./loadhandler.md).

## See Also

### Registering data
- [func registerDataRepresentation(forTypeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](./registerdatarepresentation%28fortypeidentifier,visibility,loadhandler%29.md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerItem(forTypeIdentifier: String, loadHandler: NSItemProvider.LoadHandler)](./registeritem%28fortypeidentifier,loadhandler%29.md)
  Lazily registers an item, according to the item provider type coercion policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentationforcontenttype:visibility:loadhandler:)*