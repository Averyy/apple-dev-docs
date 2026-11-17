# Simulating cloth bodies, materials, and forces

**Framework**: RealityKit  
**Role**: Sample Code  
**Download**: [SimulatingClothBodiesMaterialsAndForces.zip](https://docs-assets.developer.apple.com/published/a64d81192428/SimulatingClothBodiesMaterialsAndForces.zip)

Create realistic fabric motion with Reality Composer Pro.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

## Overview

Animating fabric so that it looks life-like can be a real challenge. Fabric drapes under its own weight, reacts to wind and to the surfaces it touches, and moves differently depending on what it’s made of. With cloth simulation in RealityKit, you describe a fabric’s physical properties and the forces acting on it, and the simulation computes its motion each frame.

This sample app includes three cloth demos: a curtain that ripples naturally in the airflow from a fan, an inflatable ball that holds its shape by maintaining a target volume, and a cloak that stays on an animated character as the character moves.

![A screenshot of the curtain demo. A curtain is blown backward by an oscillating floor fan, with a fan speed slider and a button for fan oscillation below the scene.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-01@2x.png)

![A screenshot of the ball demo. A crumpled, partially deflated ball rests in the corner of a box, with volume and stiffness sliders below the scene.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-02@2x.png)

![A screenshot of the cloak demo. A small character made of clay wears a cloak, with walk and spin animation buttons below the scene. Walk is selected.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-03@2x.png)

The sample sets up each demo scene in Reality Composer Pro, pinning the curtain’s top corners in place, placing the ball inside a box, and attaching the cloak to the character. Selecting a demo displays its scene along with the controls for that demo, such as the fan’s wind force, the ball’s target volume, or the character’s animations. Every demo also shares controls for the cloth’s material parameters and for global forces like gravity and wind, plus a toggle that lets you grab the cloth and drag it around the scene.

## Set up cloth in Reality Composer Pro

Each demo is a separate scene in Reality Composer Pro. A [`ClothSimulationComponent`](./clothsimulationcomponent.md) on the root entity of each scene controls the simulation for the cloth in that scene.

The sample configures a cloth entity in each scene by adding a [`ClothBodyComponent`](./clothbodycomponent.md) to it. The component’s Simulation Mesh field specifies the mesh that the simulation acts on, and the entity’s [`ModelComponent`](./modelcomponent.md) renders the cloth.

![A screenshot of the Reality Composer Pro editor showing the curtain scene. A square curtain mesh is selected in the viewport, and the inspector shows the curtain's cloth body component with its simulation mesh set to curtain, above a model component whose mesh resource is also set to curtain.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-04@2x.png)

The sample uses the same mesh for the cloth body and the model, so the rendered cloth matches the simulation exactly.

> **Note**: A cloth body and its model component can use different meshes. For example, pairing a detailed visual mesh with a simpler simulation mesh reduces simulation cost while keeping the rendered cloth smooth.

Cloth simulation represents each vertex of the simulation mesh as a particle. Forces and constraints act on these particles, and the cloth deforms as they move.

## Pin cloth particles with motion types

The sample suspends the cloth curtain from its corners by setting the [`motionTypes`](./clothbodycomponent/motiontypes.md) property for the particles in its top-left and -right corners to [`kinematic`](./clothbodycomponent/particlemotiontype/kinematic.md). A `kinematic` particle doesn’t move with cloth simulation, while a [`dynamic`](./clothbodycomponent/particlemotiontype/dynamic.md) particle does. The default motion type for every particle is `dynamic`.

In Reality Composer Pro, the sample configures the cloth body’s motion types by painting them directly onto the vertices of the cloth mesh with the Paint Motion Types tool. Vertices with `dynamic` motion types appear red, while vertices with `kinematic` motion types appear blue.

![A screenshot of Reality Composer Pro with the Paint Motion Types tool active on the curtain's mesh. The mesh's vertices appear as red cubes, indicating a dynamic motion type. A blue brush circle sits over the top-right corner vertex, which appears as a blue cube because the tool set its motion type to kinematic.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-05@2x.png)

With its `motionTypes` set, the curtain hangs from its top corners and the rest of the fabric drapes under gravity.

![A rendering of the curtain hanging from its top corners, with the fabric sagging between them and draping downward.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-06@2x.png)

## Attach cloth to an animated character

To make the cloak look natural when worn by the animated character, the sample ensures the cloth can collide with the character’s body and stay attached to it as the character moves.

[Video: A screen recording of the cloak demo. The character plays the spin animation, and the cloak swings outward and flutters around the character before settling back against its body when the animation ends.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-07.mp4)

In Reality Composer Pro, the sample adds a [`ClothColliderComponent`](./clothcollidercomponent.md) to the character and sets its Simulation Mesh to an optimized version of the entity’s visual mesh. The sample gives the collider a small bias, which pushes the collider’s surface slightly outward along its normals so the cloak doesn’t visibly intersect with the character’s model.

![A screenshot of the character's cloth collider in Reality Composer Pro, shown as a dense triangle wireframe that extends outward from its visual mesh in all directions by a small amount.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-08@2x.png)

> 💡 **Tip**: For the best performance, give the simulation mesh evenly sized triangles, and export it from your 3D modeling app with smooth normals and no UVs so seams don’t split its vertices.

Because the collider and the model component are on the same entity, the collider’s mesh follows the visual mesh as it deforms with the character’s skeletal animation.

To keep the cloak attached, the sample binds the cloth body to the character’s collider. In the cloth body component’s Collider To Follow section, the sample sets Collider Entity to the character’s entity. When the simulation starts, each cloth vertex binds to the nearest triangle of the collider.

The sample then uses the Paint Distance Limits tool to set a distance limit of zero for the vertices around the cloak’s neckline. A distance limit controls how far a vertex can move from its bound position, so these vertices stay fixed to the character’s neck while the rest of the cloak moves freely.

![A screenshot of Reality Composer Pro with the paint distance limits tool active on the cloak mesh. A brush circle sits over the vertices along the cloak's neckline, beneath the character's head. The inspector shows the collider to follow section enabled, with the collider entity set to root.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-09@2x.png)

In Swift, these settings correspond to the cloth body component’s [`colliderBinding`](./clothbodycomponent/colliderbinding-swift.property.md) property. Its [`sourceCollider`](./clothbodycomponent/colliderbinding-swift.struct/sourcecollider.md) property holds the collider entity, and its [`distanceLimits`](./clothbodycomponent/colliderbinding-swift.struct/distancelimits.md) property holds the per-vertex distance limits.

## Apply localized forces with a force volume

The curtain demo includes a fan that blows air at the cloth. The sample creates the airflow with a [`ClothForceVolumeComponent`](./clothforcevolumecomponent.md), which applies forces to any cloth particles inside its volume.

[Video: A screen recording of the curtain demo. The fan's blades spin while it oscillates left and right, and the curtain ripples and billows in the airflow.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-10.mp4)

After loading the fan entity from the curtain scene, the sample creates a subentity with a force volume that’s as wide as the fan’s blades and extends in front of the fan:

```swift
@State private var fanSpeed: Float = 0
@State private var isFanOscillating = false

/// How far the fan blows air, in meters.
private let fanReach: Float = 1.0

/// How quickly the wind's strength varies, making the cloth flutter instead of billowing.
private let noiseFrequency: Float = 2.5

// ...

/// Adds the component that spins the fan's blades, and the force volume that blows wind at the cloth.
private func setUp(fanBlades: Entity) {
    // Create a cloth force volume to simulate the air the fan blades blow at the cloth.
    let fanWindVolume = Entity()
    let fanDiameter = fanBlades.visualBounds(relativeTo: fanBlades).boundingRadius * 2
    var forceVolume = ClothForceVolumeComponent(shape: .box(ClothBoxShape(size: [fanDiameter, fanDiameter, fanReach])))
    forceVolume.noiseFrequency = noiseFrequency
    fanWindVolume.components.set(forceVolume)

    // Position the volume in front of the fan blades.
    fanWindVolume.position.z = fanReach / 2
    fanBlades.addChild(fanWindVolume)
    
    // Add a fan component to make the fan blades spin.
    fanBlades.components.set(FanComponent(speed: fanSpeed, isOscillating: isFanOscillating))
}
```

A slider in the demo’s controls sets the speed on the fan’s `FanComponent`. Each frame, the sample’s `FanSystem` scales the volume’s [`windForce`](./clothforcevolumecomponent/windforce.md) and [`noiseAmplitude`](./clothforcevolumecomponent/noiseamplitude.md) by that speed:

```swift
// Scale the fan's wind force and noise amplitude with its speed.
if var forceVolume = fanWindVolume.components[ClothForceVolumeComponent.self] {
    forceVolume.windForce = [0, 0, fan.maximumWindForce * fan.speed]
    forceVolume.noiseAmplitude = fan.maximumNoiseAmplitude * fan.speed
    fanWindVolume.components.set(forceVolume)
}
```

The volume’s noise adds turbulence, so the curtain ripples instead of moving uniformly.

## Inflate a watertight cloth body

The ball demo inflates a cloth body and lets you adjust its volume and stiffness while the simulation runs.

[Video: A screen recording of the ball demo. As the volume slider moves below 100 percent, the ball collapses into a deflated, wrinkled heap on the floor of the box. As the slider moves back up past 100 percent, the ball re-inflates into a round sphere.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-11.mp4)

To inflate a cloth body, the sample sets the body’s [`inflationConstraint`](./clothbodycomponent/inflationconstraint-swift.property.md), which makes the body try to keep a target volume. Inflation only works on a cloth body with a watertight mesh, meaning a closed mesh with no holes that encloses a volume.

An inflation constraint has a target volume, and a stiffness between `0` and `1` that controls how strongly the body resists changing volume. Rather than setting the constraint directly from its sliders, the sample stores the values in its own `ClothInflationEasingComponent`, which records the target volume as a multiple of the mesh’s rest volume:

```swift
/// A component that holds a cloth body at a multiple of its rest volume.
struct ClothInflationEasingComponent: Component {
    /// The multiple of the cloth body's rest volume that the body inflates toward.
    var targetVolumeScale: Float {
        didSet { needsUpdate = true }
    }

    /// How strongly the inflation constraint holds the body at its volume.
    var stiffness: Float {
        didSet { needsUpdate = true }
    }

    /// How long the body takes to cover half of the remaining distance to `targetVolumeScale`, in seconds.
    var easeHalfLife: Float = 0.15

    /// The volume of the body's mesh.
    fileprivate let restVolume: Float

    /// The multiple of `restVolume` that the body currently inflates to, which eases toward ``targetVolumeScale``.
    fileprivate var volumeScale: Float

    /// Whether the cloth body's inflation constraint is out of date.
    fileprivate var needsUpdate = true

    // ...
}
```

When the ball scene loads, the demo reads the rest volume from the cloth body’s mesh and adds the component to the ball:

```swift
// Find the ball's root entity and inflate it.
guard let ball = ballScene.findEntity(named: "Ball"),
      let restVolume = ball.components[ClothBodyComponent.self]?.mesh.volume else { return }
ball.components.set(ClothInflationEasingComponent(restVolume: restVolume, volumeScale: inflationScale, stiffness: inflationStiffness))
```

The demo’s Volume and Stiffness sliders write their values to the ball’s component instead of to the cloth body, which marks the inflation constraint as out of date:

```swift
inflationControlRow("Volume", value: $inflationScale, in: 0...2, format: .percent.precision(.fractionLength(0)))
    .onChange(of: inflationScale) {
        clothBall?.components[ClothInflationEasingComponent.self]?.targetVolumeScale = inflationScale
    }
```

The sample’s `ClothInflationEasingSystem` then eases the body’s volume toward the target over several frames and writes the result into the cloth body’s inflation constraint:

```swift
// Ease the volume the body inflates to toward its target.
let easeFactor = 1 - exp2(-deltaTime / inflation.easeHalfLife)
inflation.volumeScale = simd_mix(inflation.volumeScale, inflation.targetVolumeScale, easeFactor)
if abs(inflation.volumeScale - inflation.targetVolumeScale) < 0.001 {
    inflation.volumeScale = inflation.targetVolumeScale
    inflation.needsUpdate = false
}

clothBody.inflationConstraint = ClothBodyComponent.InflationConstraint(targetVolume: inflation.restVolume * inflation.volumeScale,
                                                                       stiffness: inflation.stiffness)
```

Easing the volume avoids a sudden jump in the constraint, ensuring the ball inflates and deflates smoothly as the target volume changes. When the volume reaches its target, the system clears `needsUpdate` so it stops writing to the cloth body until a slider moves again.

## Adjust cloth simulation and material settings

Each demo in the sample shares the same [`ClothSimulationComponent`](./clothsimulationcomponent.md) parameters and [`ClothBodyMaterial`](./clothbodymaterial.md). The sample initializes the shared simulation parameters and material in its observable `ClothSettings` class:

```swift
/// The simulation and material settings that all of the cloth demos share.
@Observable
final class ClothSettings {
    /// The acceleration that gravity applies to the cloth.
    var gravity = SIMD3<Float>(0, -9.81, 0)

    /// The force that wind applies to the cloth.
    var wind = SIMD3<Float>.zero

    /// How quickly the cloth loses energy as it moves.
    ///
    /// A small amount of damping lets the cloth come to rest after it moves, without looking sluggish.
    var dampingFactor: Float = 0.002

    /// The material that every cloth body in the simulation uses.
    var material = ClothBodyMaterial()

    // ...

    /// The name that the cloth bodies use to look up their material in the simulation component.
    ///
    /// Every body uses the same name, so changing the material updates all of the cloth simultaneously.
    private static let materialName = "Cloth"

    // ...

    /// Applies the current settings to the cloth simulation root.
    func apply(to simulationRoot: Entity) {
        guard var simulation = simulationRoot.components[ClothSimulationComponent.self] else { return }
        simulation.gravity = gravity
        simulation.wind = wind
        simulation.dampingFactor = dampingFactor
        simulation.materials[Self.materialName, ClothBodyMaterial.self] = material
        simulationRoot.components.set(simulation)
    }
}
```

The sample’s `SimulationSettingsView` binds the sample’s `VectorSlider` and `ParameterSlider` controls to the shared simulation settings:

```swift
@Bindable var clothSettings = clothSettings
VectorSlider("Gravity", value: $clothSettings.gravity, in: -20...20, defaultValue: [0, -9.81, 0])
VectorSlider("Wind", value: $clothSettings.wind, in: -0.05...0.05, fractionLength: 3)
ParameterSlider("Damping", value: $clothSettings.dampingFactor, in: 0...0.05, fractionLength: 3)
```

The sample’s `MaterialSettingsView` does the same for material settings:

```swift
/// The smallest spring and cross-tether stiffness that the sliders allow.
///
/// Keeping this value greater than zero prevents the cloth from completely losing its shape.
private static let minimumStiffness: Float = 0.01

// ...

@Bindable var clothSettings = clothSettings
// ...
ParameterSlider("Spring Stiffness", value: $clothSettings.material.springStiffness,
                in: Self.minimumStiffness...1)
ParameterSlider("Bend Stiffness", value: $clothSettings.material.bendStiffness)
ParameterSlider("Cross Tether Stiffness", value: $clothSettings.material.crossTetherStiffness,
                in: Self.minimumStiffness...1)
ParameterSlider("Laplacian Damping", value: $clothSettings.material.laplacianDamping)
ParameterSlider("Static Friction", value: $clothSettings.material.staticFriction, in: 0...2)
ParameterSlider("Kinetic Friction", value: $clothSettings.material.kineticFriction, in: 0...2)
```

Every demo shares the sample’s `ClothDemoSceneView`, which loads the demo’s scene and passes the scene’s root entity to `assignMaterial(to:)`. That method assigns the shared material to all the cloth bodies in that entity’s hierarchy by name.

```swift
/// Assigns the shared material to every cloth body in the entity's hierarchy.
func assignMaterial(to entity: Entity) {
    entity.components[ClothBodyComponent.self]?.materialNames = [Self.materialName]
    for subentity in entity.children {
        assignMaterial(to: subentity)
    }
}
```

Whenever the settings change, `ClothDemoSceneView` applies them to the scene’s simulation root in the `update` closure of its [`RealityView`](./realityview.md).

```swift
RealityView { content in
    // ...
} update: { _ in
    // Apply the latest settings to the scene's cloth simulation.
    if let simulationRoot {
        clothSettings.apply(to: simulationRoot)
    }
}
```

## Tune materials to mimic real fabrics

The sample includes a material picker that lets you choose from preset cloth materials. Choosing a preset updates the shared material in `ClothSettings`, which updates every cloth body in the current demo.

Each preset configures the six parameters on a [`ClothBodyMaterial`](./clothbodymaterial.md):

- [`springStiffness`](./clothbodymaterial/springstiffness.md) is the resistance to stretching and compressing between adjacent particles, from `0` to `1`. Lowering it from its default of `1` lets the fabric stretch and sag under its own weight.
- [`bendStiffness`](./clothbodymaterial/bendstiffness.md) is the resistance to bending between adjacent triangles, from `0` to `1`. Its default is `0`, and raising it makes the fabric form broader folds and hold its shape.
- [`crossTetherStiffness`](./clothbodymaterial/crosstetherstiffness.md) is the resistance to shearing between opposing particles, from `0` to `1`. Its default is `0.25`, and raising it prevents the fabric from skewing.
- [`laplacianDamping`](./clothbodymaterial/laplaciandamping.md) damps each particle’s velocity based on the velocities of the particles it connects to, from `0` to `1`. Its default is `0.1`, and raising it makes the fabric settle more quickly, like a wet cloth.
- [`staticFriction`](./clothbodymaterial/staticfriction.md) is the friction a particle experiences against a collider or another particle that it isn’t moving relative to, which determines how readily the fabric starts to slide. It’s non-negative and defaults to `0.8`.
- [`kineticFriction`](./clothbodymaterial/kineticfriction.md) is the friction a particle experiences when it’s already sliding, which determines how quickly the fabric drags to a stop. It’s non-negative and defaults to `0.7`.

The sample extends `ClothBodyMaterial` with an initializer that takes all six parameters, so each preset can set them in a single expression:

```swift
extension ClothBodyMaterial {
    /// Creates a cloth body material with the stiffness, damping, and friction values you specify.
    init(springStiffness: Float, bendStiffness: Float, crossTetherStiffness: Float,
         laplacianDamping: Float, staticFriction: Float, kineticFriction: Float) {
        self.init()
        self.springStiffness = springStiffness
        self.bendStiffness = bendStiffness
        self.crossTetherStiffness = crossTetherStiffness
        self.laplacianDamping = laplacianDamping
        self.staticFriction = staticFriction
        self.kineticFriction = kineticFriction
    }
}
```

With that initializer in place, the sample defines its presets in `ClothMaterialPreset.swift`, combining these parameters to mimic the drape and feel of real fabrics:

```swift
case .default:
    ClothBodyMaterial()
case .silk:
    // Low bend stiffness and friction, so it falls in soft
    // folds and slides easily.
    ClothBodyMaterial(springStiffness: 1, bendStiffness: 0.01,
                      crossTetherStiffness: 0.1, laplacianDamping: 0.05,
                      staticFriction: 0.25, kineticFriction: 0.2)
case .knitWool:
    // Low spring stiffness and high friction, so it stretches,
    // sags, and clings to what it touches.
    ClothBodyMaterial(springStiffness: 0.4, bendStiffness: 0.18,
                      crossTetherStiffness: 0.15, laplacianDamping: 0.25,
                      staticFriction: 1.2, kineticFriction: 1)
case .velvet:
    // The highest damping and friction, so it settles quickly
    // and drags against surfaces.
    ClothBodyMaterial(springStiffness: 1, bendStiffness: 0.2,
                      crossTetherStiffness: 0.3, laplacianDamping: 0.65,
                      staticFriction: 1.4, kineticFriction: 1.2)
case .linen:
    // Higher bend stiffness than silk, wool, or velvet,
    // and the lowest damping, so it holds folds but still ripples freely.
    ClothBodyMaterial(springStiffness: 1, bendStiffness: 0.25,
                      crossTetherStiffness: 0.3, laplacianDamping: 0.02,
                      staticFriction: 0.7, kineticFriction: 0.6)
case .denim:
    // High bend and cross-tether stiffness, so it forms broad folds.
    ClothBodyMaterial(springStiffness: 1, bendStiffness: 0.4,
                      crossTetherStiffness: 0.45, laplacianDamping: 0.15,
                      staticFriction: 1, kineticFriction: 0.85)
case .leather:
    // The highest bend stiffness, so it resists bending and
    // keeps its shape.
    ClothBodyMaterial(springStiffness: 1, bendStiffness: 0.8,
                      crossTetherStiffness: 0.7, laplacianDamping: 0.3,
                      staticFriction: 1.2, kineticFriction: 1)
}
```

> **Note**: The sample tunes these values for how they look in its demos. Use them as starting points rather than physical constants.

## Grab and drag the cloth with a ray

When you turn on cloth interaction, you can grab the cloth in each demo and drag it around the scene.

[Video: A screen recording of the curtain demo with cloth interaction on. A pointer grabs the center of the curtain, drags it right and left, and then throws it upward before releasing it.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/simulating-cloth-bodies-materials-and-forces-12.mp4)

The sample’s `ClothGrabber` class creates a grab entity with a [`ClothGrabComponent`](./clothgrabcomponent.md) in ray mode:

```swift
private let grabEntity = Entity(components: [ClothGrabComponent(mode: .ray)])
```

In ray mode, the component grabs the cloth particles that a ray from the entity’s position, along its forward (-Z) axis, intersects.

The `grab(along:)` method points the grab entity along a ray in scene space and sets the component’s [`isGrabbing`](./clothgrabcomponent/isgrabbing.md) property to `true`. The `release()` method sets it back to `false`:

```swift
/// Aims the grabber along `ray`, in scene space, and grabs the cloth particles that the ray intersects.
func grab(along ray: (origin: SIMD3<Float>, direction: SIMD3<Float>)) {
    grabEntity.look(at: ray.origin + ray.direction, from: ray.origin, relativeTo: nil)
    if var grab = grabEntity.components[ClothGrabComponent.self], !grab.isGrabbing {
        grab.isGrabbing = true
        grabEntity.components.set(grab)
    }
}

/// Releases the cloth particles that the grabber holds back to the simulation.
func release() {
    grabEntity.components[ClothGrabComponent.self]?.isGrabbing = false
}
```

When `isGrabbing` changes to `true`, the component selects the particles that the ray intersects. While it stays `true`, the component drags those particles to follow the ray, so aiming along a new ray on every gesture update pulls the cloth along. When it changes to `false`, the component releases the particles back to the simulation.

After `ClothDemoSceneView` loads a demo’s scene, it calls the grabber’s `attach(to:in:)` method, which adds the grab entity to that scene. On iOS, iPadOS, and macOS it also keeps the view content for projecting gestures into the scene. On visionOS it adds an input target that spans the scene:

**iOS and macOS**:

```swift
/// The reality view content that projects a gesture's location into a ray through the scene.
private(set) var content: RealityViewCameraContent?

/// Adds the grabber to the entity's hierarchy, and keeps `content` for projecting gestures
/// into that entity's scene.
func attach(to entity: Entity, in content: RealityViewCameraContent) {
    entity.addChild(grabEntity)
    self.content = content
}
```

**visionOS**:

```swift
/// An invisible input target entity that spans the entire scene.
///
/// This allows a pinch anywhere in the scene to aim and move the grabber.
let inputTarget = Entity(components: [InputTargetComponent()])

/// Adds the grabber and the input target to the entity's hierarchy.
func attach(to entity: Entity, in content: RealityViewContent) {
    entity.addChild(grabEntity)
    let bounds = entity.visualBounds(relativeTo: entity)
    let shape = ShapeResource.generateBox(size: bounds.extents).offsetBy(translation: bounds.center)
    inputTarget.components.set(CollisionComponent(shapes: [shape]))
    entity.addChild(inputTarget)
}
```

The sample drives the cloth grabber with [`DragGesture`](../SwiftUI/draggesture.md) on iOS, iPadOS, and macOS, and with [`SpatialEventGesture`](../SwiftUI/spatialeventgesture.md) on visionOS:

**iOS and macOS**:

```swift
DragGesture(minimumDistance: 0, coordinateSpace: .local)
    .onChanged { value in
        // Aim the grabber along the ray through the drag's location.
        guard let ray = grabber.content?.ray(through: value.location, in: .local, to: .scene) else { return }
        grabber.grab(along: ray)
    }
    .onEnded { _ in
        // Release the cloth when the drag ends.
        grabber.release()
    }
```

**visionOS**:

```swift
/// The gesture that's currently grabbing the cloth.
@State private var gesture: (id: SpatialEventCollection.Event.ID, offset: SIMD3<Float>, direction: SIMD3<Float>)?

// ...

SpatialEventGesture()
    .targetedToEntity(grabber.inputTarget)
    .onChanged { value in
        if let gesture {
            // Follow only the gesture that started the grab, and let go when it ends.
            guard let pinch = value.gestureValue[gesture.id], pinch.phase == .active else {
                grabber.release()
                self.gesture = nil
                return
            }

            // Translate the ray's origin with the gesture, keeping its original direction.
            let location = value.convert(pinch.location3D, from: .local, to: .scene)
            grabber.grab(along: (origin: location + gesture.offset, direction: gesture.direction))
        } else if let pinch = value.gestureValue.first(where: { $0.phase == .active }),
                  let ray = pinch.selectionRay {
            // Grab cloth along the gesture's selection ray.
            let location = value.convert(pinch.location3D, from: .local, to: .scene)
            let origin = value.convert(ray.origin, from: .local, to: .scene)
            let direction = value.convert(ray.direction, from: .local, to: .scene)
            grabber.grab(along: (origin: origin, direction: direction))
            gesture = (id: pinch.id, offset: origin - location, direction: direction)
        }
    }
    .onEnded { _ in
        // Release the cloth when the gesture ends.
        grabber.release()
        gesture = nil
    }
```

On visionOS, the system populates [`selectionRay`](../SwiftUI/spatialeventcollection/event/selectionray.md) only while your app has an immersive space open.

## See Also

### Simulation and bodies
- [struct ClothSimulationComponent](./clothsimulationcomponent.md)
  A component that marks an entity as the simulation root of a localized cloth simulation.
- [struct ClothBodyComponent](./clothbodycomponent.md)
  A component that simulates an entity as a deformable cloth body, when part of a cloth simulation.
- [struct ClothBodyMaterial](./clothbodymaterial.md)
  A struct that represents a cloth body’s material.
- [struct ClothGrabComponent](./clothgrabcomponent.md)
  A component that grabs and drags particles of cloth bodies using either a ray or a volume, as determined by the `mode` property.
- [struct ClothForceVolumeComponent](./clothforcevolumecomponent.md)
  A component that creates a force volume applying forces to any intersecting cloth body particles.
- [struct ClothQueryVolumeComponent](./clothqueryvolumecomponent.md)
  A component that defines a volume for querying particles of cloth bodies.
- [struct ClothCoordinateSpace](./clothcoordinatespace.md)
  Defines a reference frame within a cloth simulation.
- [struct PerClothVertexData](./perclothvertexdata.md)
  A generic type that stores per-vertex data in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simulating-cloth-bodies-materials-and-forces)*