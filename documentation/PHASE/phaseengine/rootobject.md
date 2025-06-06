# rootObject

**Framework**: PHASE  
**Kind**: property

The main object to which the app adds child objects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var rootObject: PHASEObject { get }
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Discussion

The framework creates and sets the root object at engine instantiation.

Avoid executing the following actions in your app; these actions cause the engine to generate a runtime error:

- Adding this object as a child.
- Altering the transform of this object.
- Copying this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/rootobject)*