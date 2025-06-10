# handle(_:forProperties:handler:)

**Framework**: SceneKit  
**Kind**: method

Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.

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
func handle(_ event: SCNParticleEvent, forProperties properties: [SCNParticleSystem.ParticleProperty], handler block: @escaping SCNParticleEventBlock)
```

#### Discussion

By associating a block with one or more particle properties, you can run arbitrary code that modifies those properties when a significant event in the particle simulation occurs for one or more particles. For example, you can use the following code with a confetti effect to randomly switch between two distinct colors for each spawned particle:

```objc
[system handleEvent:SCNParticleEventBirth
      forProperties:@[SCNParticlePropertyColor]
          withBlock:^(void **data, size_t *dataStride, uint32_t *indices , NSInteger count) {
              for (NSInteger i = 0; i < count; ++i) {
                  float *color = (float *)((char *)data[0] + dataStride[0] * i);
                  if (rand() & 0x1) { // Switch the green and red color components.
                      color[0] = color[1];
                      color[1] = 0;
                  }
              }
          }];
```

## Parameters

- `event`: The event at which to call the block. See   for allowed values.
- `properties`: An array containing one or more of the constants listed in  , each of which specifies a property of the appearance or behaviors of particles in the particle system.
- `block`: A   block to be called every time SceneKit renders a frame. In this block you can modify the properties of particles in the system.

## See Also

- [enum SCNParticleEvent](scnparticleevent.md)
  Significant events in the life spans of simulate particles, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.
- [typealias SCNParticleEventBlock](scnparticleeventblock.md)
  The signature for blocks called by SceneKit in response to significant events during particle simulation, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/handle(_:forproperties:handler:))*