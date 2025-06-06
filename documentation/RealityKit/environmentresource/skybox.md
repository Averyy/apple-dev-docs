# skybox

**Framework**: RealityKit  
**Kind**: property

The cube color texture that contains environment surrounding details.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var skybox: TextureResource { get }
```

#### Discussion

The skybox contains the environment’s detailed surroundings as a cube texture, which you can use to render the background of a scene. The skybox texture determines the environment’s lighting. You can assign the skybox texture to a [`ShaderGraphMaterial`](shadergraphmaterial.md) cube texture parameter.

```swift
// Load an environment resource.
let env = try await EnvironmentResource(
    named: environmentResourceName, in: Bundle.main)

// Assign its skybox to a material's cube map texture parameter.
var skyboxCubeMaterial = try await ShaderGraphMaterial(named: materialUSDPath,
                                                       from: sceneResourceName,
                                                       in: contentBundle)
try await skyboxCubeMaterial.setParameter(name: cubeTextureParameterName,
                                          value: .textureResource(env.skybox))
skyboxCubeMaterial.faceCulling = .front

// Apply to a background sky dome sphere.
let skyDome = await ModelEntity(mesh: .generateSphere(radius: 1E3),
                                materials: [skyboxCubeMaterial])

await MainActor.run {
    sceneRootEntity.addChild(skyDome)

    // Also use the environment resource for lighting.
    let probe = VirtualEnvironmentProbeComponent.Probe(environment: env)
    sceneRootEntity.components.set(VirtualEnvironmentProbeComponent(source: .single(probe)))
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/skybox)*