# init(contents:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a new material property object with the specified contents.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
convenience init(contents: Any)
```

```objc
+ (instancetype) materialPropertyWithContents:(id) contents;
```

## Return Value

A new material property object.

## Discussion

Newly created [`SCNMaterial`](../scnmaterial.md) objects contain [`SCNMaterialProperty`](../scnmaterialproperty.md) instances for all of their visual properties. To change a material’s visual properties, you modify those instances rather than creating new material property objects.

You create new [`SCNMaterialProperty`](../scnmaterialproperty.md) instances to provide textures for use with custom GLSL shaders—for details, see [`SCNShadable`](../scnshadable.md).

## Parameters

- `contents`: The visual contents of the material property—a color, image, or source of animated content. For details, see the discussion of the  [`contents`](./contents.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/init(contents:))*