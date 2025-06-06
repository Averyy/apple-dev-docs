# registerObject(_:visibility:)

**Framework**: Foundation  
**Kind**: method

Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.

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
func registerObject(_ object: any NSItemProviderWriting, visibility: NSItemProviderRepresentationVisibility)
```

#### Discussion

If a representation for a given UTI is already registered, it is preserved (specifically, duplicate representations are ignored).

## See Also

- [func registerObject(ofClass: any NSItemProviderWriting.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: (((any NSItemProviderWriting)?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn.md)
  Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject<T>(ofClass: T.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((T?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-133rx.md)
  Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func register<T>(@autoclosure () -> T)](nsitemprovider/register(_:).md)
  Adds representations of a specified transferable type to an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerobject(_:visibility:))*