# init(engine:mesh:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates an object that the given geometric data shapes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine, mesh: MDLMesh)
```

```objc
- (instancetype) initWithEngine:(PHASEEngine *) engine mesh:(MDLMesh *) mesh;
```

## Parameters

- `engine`: The object that controls this class’s associated audio output.
- `mesh`: A collection of points that connect to form a shape.

## See Also

### Creating a Shape
- [convenience init(engine: PHASEEngine, mesh: MDLMesh, materials: [PHASEMaterial])](./init%28engine,mesh,materials%29.md)
  Creates an object of a specific material that the given geometric data shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseshape/init(engine:mesh:))*