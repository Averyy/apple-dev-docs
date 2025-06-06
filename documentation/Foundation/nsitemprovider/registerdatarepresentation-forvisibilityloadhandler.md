# registerDataRepresentation(for:visibility:loadHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a data-backed representation for an item, specifiying item visibility and a load handler.

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
func registerDataRepresentation(for contentType: UTType, visibility: NSItemProviderRepresentationVisibility = .all, loadHandler: @escaping (@escaping (Data?, (any Error)?) -> Void) -> Progress?)
```

## See Also

- [func registerDataRepresentation(forTypeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerItem(forTypeIdentifier: String, loadHandler: NSItemProvider.LoadHandler)](nsitemprovider/registeritem(fortypeidentifier:loadhandler:).md)
  Lazily registers an item, according to the item provider type coercion policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:))*