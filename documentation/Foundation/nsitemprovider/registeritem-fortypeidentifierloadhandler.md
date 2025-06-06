# registerItem(forTypeIdentifier:loadHandler:)

**Framework**: Foundation  
**Kind**: method

Lazily registers an item, according to the item provider type coercion policy.

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
func registerItem(forTypeIdentifier typeIdentifier: String, loadHandler: @escaping NSItemProvider.LoadHandler)
```

#### Discussion

Use this method to register blocks that can take the item provider’s file or data object and convert it to a specific data format. Your `loadHandler` block is executed when a client passes the same `typeIdentifier` string to the [`loadItem(forTypeIdentifier:options:completionHandler:)`](nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:).md) method. In the implementation of your block, coerce the data to the specified type and call the provided completion handler. You must call the completion handler, either with the requested data or with an error.

Item providers know how to coerce known types of objects, such as images or strings. Use this method to register blocks to coerce your custom data types.

## Parameters

- `typeIdentifier`: A string that represents the desired UTI.
- `loadHandler`: A block capable of returning the data item as the specified type. For information about implementing this block, see  .

## See Also

- [func registerDataRepresentation(forTypeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerDataRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registeritem(fortypeidentifier:loadhandler:))*