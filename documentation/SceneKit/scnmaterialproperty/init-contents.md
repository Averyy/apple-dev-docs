# init(contents:)

**Framework**: SceneKit  
**Kind**: init

Creates a new material property object with the specified contents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(contents: Any)
```

#### Return Value

A new material property object.

#### Discussion

Newly created [`SCNMaterial`](scnmaterial.md) objects contain [`SCNMaterialProperty`](scnmaterialproperty.md) instances for all of their visual properties. To change a material’s visual properties, you modify those instances rather than creating new material property objects.

You create new [`SCNMaterialProperty`](scnmaterialproperty.md) instances to provide textures for use with custom GLSL shaders—for details, see [`SCNShadable`](scnshadable.md).

## Parameters

- `contents`: The visual contents of the material property—a color, image, or source of animated content. For details, see the discussion of the    property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/init(contents:))*