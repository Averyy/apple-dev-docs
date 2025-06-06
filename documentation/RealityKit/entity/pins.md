# pins

**Framework**: RealityKit  
**Kind**: property

The entity’s geometric pins.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
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

Entities with skeletal poses expose skeletal pose joints as [`GeometricPin`](geometricpin.md) instances. These pins are not stored in the [`GeometricPinsComponent`](geometricpinscomponent.md) on the [`Entity`](entity.md), but are obtained directly from the skeletal pose.

The name of the [`GeometricPin`](geometricpin.md) is the name of the skeletal pose joint. The pose (position and orientation) of the [`GeometricPin`](geometricpin.md) is the current pose of the joint in the coordinate frame of the [`Entity`](entity.md) (i.e.  relative to the parent joint). While the skeletal pose is animated, the [`GeometricPin`](geometricpin.md) pose change on every frame.

The geometric pin’s [`name`](geometricpin/name.md) can be given as either the full skeletal pose joint path name, such as `"root/hips_joint/spine_1_joint/spine_2_joint"`, or as the leaf joint name, like `"spine_2_joint"`.

For example, get a pin via a full pose joint name, or with its leaf joint name:

```swift
let jointPinFromFullName = skeletalPoseEntity.pins["root/hips_joint/spine_1_joint/spine_2_joint"]
let jointPinFromShortName = skeletalPoseEntity.pins["spine_2_joint"]
```

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
let myJointPinEscaped = skeletalPoseEntity.pins["my\\.joint"]
// Alternatively, use Swift's raw string feature
// by enclosing the string in # symbols.
let myJointPinRaw = skeletalPoseEntity.pins[#"my\.joint"#]
```

> **Note**: Character escaping is only required for skeletal pose joints.

Character escaping is only required for skeletal pose joints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/pins)*