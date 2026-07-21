# program

**Framework**: RealityKit  
**Kind**: property

The compiled program that drives this material’s surface and geometry shading.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var program: PortalMaterial.Program { get set }
```

#### Discussion

Read this property to recover the program a portal material was created with — for example, to share it with another [`PortalMaterial`](portalmaterial.md). Assign a new program to swap a portal’s shading without rebuilding the material; the material’s existing parameter bindings are preserved, and bindings whose names and types match inputs on the new program’s shader graph keep working. Bindings that don’t match are ignored at render time — re-bind any new inputs the program introduces before drawing the portal.

## See Also

- [PortalMaterial.Program](portalmaterial/program-swift.struct.md)
  A compiled shader program that drives the appearance of a portal’s surface and geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.property)*