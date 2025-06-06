# isRotationLocked

**Framework**: RealityKit  
**Kind**: property

A tuple of Boolean values that you use to lock rotation of the physics body around any of the three axes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var isRotationLocked: (x: Bool, y: Bool, z: Bool)
```

#### Discussion

For any one of the three Booleans in the tuple that you set to `true`, rotation is restricted on the axis represented by that item. For example, if you set the `x` item to true, then the body can’t rotate around the x-axis. By default, rotation isn’t restricted.

## See Also

- [var isTranslationLocked: (x: Bool, y: Bool, z: Bool)](physicsbodycomponent/istranslationlocked.md)
  A tuple of Boolean values that you use to lock the position of the physics body along any of the three axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/isrotationlocked)*