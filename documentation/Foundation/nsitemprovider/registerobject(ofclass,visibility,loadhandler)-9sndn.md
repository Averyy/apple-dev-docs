# registerObject(ofClass:visibility:loadHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.

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
func registerObject(ofClass aClass: any NSItemProviderWriting.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: @escaping @Sendable (@escaping @Sendable ((any NSItemProviderWriting)?, (any Error)?) -> Void) -> Progress?)
```

```objc
- (void) registerObjectOfClass:(Class<NSItemProviderWriting> *) aClass visibility:(NSItemProviderRepresentationVisibility) visibility loadHandler:(NSProgress * (^)(void (^completionHandler)(id<NSItemProviderWriting>object, NSError *error))) loadHandler;
```

## See Also

### Registering objects
- [func registerObject(any NSItemProviderWriting, visibility: NSItemProviderRepresentationVisibility)](./registerobject%28_,visibility%29.md)
  Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject<T>(ofClass: T.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((T?, (any Error)?) -> Void) -> Progress?)](./registerobject%28ofclass,visibility,loadhandler%29-133rx.md)
  Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func register<T>(@autoclosure () -> T)](./register%28_%29.md)
  Adds representations of a specified transferable type to an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn)*