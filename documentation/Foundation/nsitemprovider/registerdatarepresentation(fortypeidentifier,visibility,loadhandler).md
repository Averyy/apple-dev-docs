# registerDataRepresentation(forTypeIdentifier:visibility:loadHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func registerDataRepresentation(forTypeIdentifier typeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable (Data?, (any Error)?) -> Void) -> Progress?)
```

```objc
- (void) registerDataRepresentationForTypeIdentifier:(NSString *) typeIdentifier visibility:(NSItemProviderRepresentationVisibility) visibility loadHandler:(NSProgress * (^)(void (^completionHandler)(NSData *data, NSError *error))) loadHandler;
```

## See Also

### Registering data
- [func registerDataRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](./registerdatarepresentation%28for,visibility,loadhandler%29.md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerItem(forTypeIdentifier: String, loadHandler: NSItemProvider.LoadHandler)](./registeritem%28fortypeidentifier,loadhandler%29.md)
  Lazily registers an item, according to the item provider type coercion policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:))*