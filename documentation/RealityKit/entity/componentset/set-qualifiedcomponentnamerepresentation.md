# set(qualifiedComponentName:representation:)

**Framework**: RealityKit  
**Kind**: method

Adds component data to an entity which will be written to a Reality file, but have no other effect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func set(qualifiedComponentName: String, representation: some Encodable) throws
```

#### Discussion

This function allows you to set component properties which have no available definition, such as properties that are only available on some platforms, or properties which don’t have an accessible runtime Swift type.

The following built-in components support setting properties using this function:

- `AnchoringComponent`
- `DockingRegionComponent`
- `EnvironmentBlendingComponent`
- `ManipulationComponent`
- `SceneUnderstandingComponent`


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(qualifiedcomponentname:representation:))*