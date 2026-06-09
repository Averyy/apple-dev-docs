# pins

**Framework**: RealityKit  
**Kind**: property

The entity’s geometric pins.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var pins: EntityGeometricPins { get }
```

#### Discussion

You can look up, add, and remove a [`GeometricPin`](geometricpin.md) for the owning entity through this [`EntityGeometricPins`](entitygeometricpins.md) instance. The entity’s [`GeometricPinsComponent`](geometricpinscomponent.md) stores any added geometric pins.

Other [`Component`](component.md) types on an [`Entity`](entity.md) may also provide [`GeometricPin`](geometricpin.md) instances, such as for skeletal pose joints. There is no distinction between these two when [`GeometricPin`](geometricpin.md) instances are accessed.

##### Geometric Pins for Skeletal Pose Joints

Pins for skeletal pose joints are not predefined, they need to be set in entity’s GeometricPinsComponent before you can access them. When associating a pin with a skeletal pose joint, you need to pass in the correct joint names either in full pose joint name or with its leaf joint name:

```swift
let fullNamePin = skeletalPoseEntity.pins.set(named: "fullName", skeletalJointName: "root/hips_joint/spine_1_joint/spine_2_joint")
let shortNamePin = skeletalPoseEntity.pins.set(named: "shortName", skeletalJointName: "spine_2_joint")
```

The pose (position and orientation) of the [`GeometricPin`](geometricpin.md) is the current pose of the joint in the coordinate frame of the [`Entity`](entity.md) (i.e. *not* relative to the parent joint). While the skeletal pose is animated, the [`GeometricPin`](geometricpin.md) pose change on every frame.

To print all the pins, you can loop over [`pins`](entity/pins.md).

```swift
for pin in skeletalPoseEntity.pins {
    print("joint   name: \(pin.name)")        // Full joint path name.
    print("    position: \(pin.position)")    // In coordinate frame of skeletalPoseEntity.
    print(" orientation: \(pin.orientation)") // In coordinate frame of skeletalPoseEntity.
}

```

In skeletal pose joint names, prefix the characters `.`, `[`, `]` and `\` with an escaping character (`\`).

For example, to access a skeletal pose joint named `"my.joint"`:

```swift
// To include a literal backslash in a string,
// escape it with an additional backslash.
let myJointPinEscaped = skeletalPoseEntity.pins.set(named: "myJointPinEscaped", skeletalJointName: "my\\.joint")
// Alternatively, use Swift's raw string feature
// by enclosing the string in # symbols.
let myJointPinRaw = skeletalPoseEntity.pins.set(named: "myJointPinEscaped", skeletalJointName: #"my\.joint"#)
```

> **Note**: Character escaping is only required for skeletal pose joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/pins)*