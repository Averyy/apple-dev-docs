# register(_:)

**Framework**: Foundation  
**Kind**: method

Adds representations of a specified transferable type to an item provider.

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
func register<T>(_ transferable: @autoclosure @escaping () -> T) where T : Transferable
```

## See Also

- [func registerObject(any NSItemProviderWriting, visibility: NSItemProviderRepresentationVisibility)](nsitemprovider/registerobject(_:visibility:).md)
  Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject(ofClass: any NSItemProviderWriting.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: (((any NSItemProviderWriting)?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn.md)
  Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject<T>(ofClass: T.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((T?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-133rx.md)
  Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/register(_:))*