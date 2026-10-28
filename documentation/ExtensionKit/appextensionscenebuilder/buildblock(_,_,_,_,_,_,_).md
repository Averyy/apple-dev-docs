# buildBlock(_:_:_:_:_:_:_:)

**Framework**: ExtensionKit  
**Kind**: method  
**Role**: Type Method

Builds an extension scene by combining seven scenes.

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
@MainActor
@preconcurrency static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5, _ c6: C6) -> some AppExtensionScene where C0 : AppExtensionScene, C1 : AppExtensionScene, C2 : AppExtensionScene, C3 : AppExtensionScene, C4 : AppExtensionScene, C5 : AppExtensionScene, C6 : AppExtensionScene
```

## Return Value

The composed scene.

## See Also

### Building the scene’s content
- [static func buildBlock<Content>(Content) -> some AppExtensionScene](./buildblock%28_%29.md)
  Passes through a single extension scene unmodified.
- [static func buildBlock<C0, C1>(C0, C1) -> some AppExtensionScene](./buildblock%28_,_%29.md)
  Builds an extension scene by combining two scenes.
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some AppExtensionScene](./buildblock%28_,_,_%29.md)
  Builds an extension scene by combining three scenes.
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some AppExtensionScene](./buildblock%28_,_,_,_%29.md)
  Builds an extension scene by combining four scenes.
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some AppExtensionScene](./buildblock%28_,_,_,_,_%29.md)
  Builds an extension scene by combining five scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some AppExtensionScene](./buildblock%28_,_,_,_,_,_%29.md)
  Builds an extension scene by combining six scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some AppExtensionScene](./buildblock%28_,_,_,_,_,_,_,_%29.md)
  Builds an extension scene by combining eight scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some AppExtensionScene](./buildblock%28_,_,_,_,_,_,_,_,_%29.md)
  Builds an extension scene by combining nine scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some AppExtensionScene](./buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
  Builds an extension scene by combining ten scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionscenebuilder/buildblock(_:_:_:_:_:_:_:))*