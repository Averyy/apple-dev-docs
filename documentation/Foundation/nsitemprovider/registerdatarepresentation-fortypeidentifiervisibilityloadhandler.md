# registerDataRepresentation(forTypeIdentifier:visibility:loadHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a data-backed representation for an item, specifiying item visibility and a load handler.

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
func registerDataRepresentation(forTypeIdentifier typeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping (@escaping (Data?, (any Error)?) -> Void) -> Progress?)
```

## See Also

- [func registerDataRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerItem(forTypeIdentifier: String, loadHandler: NSItemProvider.LoadHandler)](nsitemprovider/registeritem(fortypeidentifier:loadhandler:).md)
  Lazily registers an item, according to the item provider type coercion policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:))*