# SCNParticleEventBlock

**Framework**: SceneKit  
**Kind**: typealias

The signature for blocks called by SceneKit in response to significant events during particle simulation, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNParticleEventBlock = (UnsafeMutablePointer<UnsafeMutableRawPointer>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UInt32>?, Int) -> Void
```

#### Discussion

The block takes the following parameters:

When SceneKit calls your handler block for the [`SCNParticleEvent.birth`](scnparticleevent/birth.md) event, you need not use this parameter—at that time, the affected particles are indexed from `0` to the `count` parameter’s value.

Use this block to change properties of individual particles when they are spawned, when they collide with scene geometry, or when they die (that is, reach the end of their life spans and are removed from the scene).

The following example illustrates setting up a handler block for particle collision events:

```objc
[system handleEvent:SCNParticleEventCollision
      forProperties:@[SCNParticlePropertyAngle,
                      SCNParticlePropertyRotationAxis,
                      SCNParticlePropertyContactNormal]
          withBlock:^(void **data, size_t *dataStride, uint32_t *indices, NSInteger count) {
              // For each particle affected by the collision event,
              // calculate pointers in the data to each property's value.
              for (NSInteger i = 0; i < count; ++i) {
                  // SCNParticlePropertyAngle (float)
                  float *angle = (float *)((char *)data[0] + dataStride[0] * indices[i]);
                  // angle[0] is the particle's rotation angle in radians.
 
                  // SCNParticlePropertyRotationAxis (float3)
                  float *axis = (float *)((char *)data[1] + dataStride[1] * indices[i]);
                  // axis[0..2] are the xyz components of the particle's rotation axis.
 
                  // SCNParticlePropertyContactNormal (float3)
                  float *norm = (float *)((char *)data[2] + dataStride[2] * indices[i]);
                  // norm[0..2] are the xyz components of the contact normal vector.
 
                  // Now, use the norm vector to rotate the particle's axis/angle (not shown).
              }
          }];
```

## See Also

- [func handle(SCNParticleEvent, forProperties: [SCNParticleSystem.ParticleProperty], handler: SCNParticleEventBlock)](scnparticlesystem/handle(_:forproperties:handler:).md)
  Adds a block that modifies particle properties, to be executed at a specified event in the lifetimes of particles in the system.
- [enum SCNParticleEvent](scnparticleevent.md)
  Significant events in the life spans of simulate particles, used by the [`handle(_:forProperties:handler:)`](scnparticlesystem/handle(_:forproperties:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleeventblock)*