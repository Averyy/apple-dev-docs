# offsetOrientation

**Framework**: RealityKit  
**Kind**: property

Offset from the pin’s base orientation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var offsetOrientation: simd_quatf { get set }
```

#### Discussion

If a pin has a generic name, this offset is relative to the pin’s owning entity’s orientation. If a pin is on a skeletal joint, this offset is relative to the skeletal joint’s current orientation. By default this offset is the identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/geometricpin/offsetorientation)*