# hidden

**Framework**: Model I/O  
**Kind**: property

A Boolean value indicating whether this object should be used in rendering.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var hidden: Bool { get set }
```

#### Discussion

Model I/O is not a renderer, so this property is purely informational.

Renderers using assets imported using Model I/O can use this property to determine whether to include meshes in a rendered scene, apply lighting from light sources, and so on.

## See Also

- [var instance: MDLObject?](mdlobject/instance.md)
  The primary object, if applicable, of which this object is an instance.
- [var path: String](mdlobject/path.md)
  A path that identifies the object in an asset’s object hierarchy using object names.
- [var components: [any MDLComponent]](mdlobject/components.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlobject/hidden)*