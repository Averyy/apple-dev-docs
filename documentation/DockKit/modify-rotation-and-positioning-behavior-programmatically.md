# Modify rotation and positioning programmatically

**Framework**: DockKit

Perform custom control of the dock accessory.

#### Overview

You can implement your own inference and tracking to directly control the velocity or position of the docking station. To do this, use [`setSystemTrackingEnabled(_:)`](dockaccessorymanager/setsystemtrackingenabled(_:).md) to prevent system from automatically tracking subjects.

```swift
do {
    try await DockAccessoryManager.shared.setSystemTrackingEnabled(false)
} catch {
   // Handle any errors.
}
```

After disabling tracking, use [`accessoryStateChanges`](dockaccessorymanager/accessorystatechanges.md) to iterate through the available accessories and find the one you wish to interact with.

Once you identify the accessory of interest use [`setAngularVelocity(_:)`](dockaccessory/setangularvelocity(_:).md), [`setOrientation(_:duration:relative:)`](dockaccessory/setorientation(_:duration:relative:)-2epe2.md) and [`setOrientation(_:duration:relative:)`](dockaccessory/setorientation(_:duration:relative:)-6b0fl.md) to directly control the speed and position of the accessory:

```swift
do {
    // Set angular velocity in radians per second.
    // On iOS, pitch is downwards.
    let vector = Vector3D(x: pitch, y: yaw, z: roll)
    try await dockAccessory.setAngularVelocity(vector)

    // Set rotational position and wait for updates as the accessory executes a trajectory.
    let rotation = Rotation3D(eulerAngles: EulerAngles(x: Angle2D(radians: yaw), y: Angle2D(radians: pitch), z: Angle2D(radians: roll), order: __SPEulerAngleOrder.xyz))
    // NOTE: You can also initialize from quaternions:
    // let pos = Rotation3D(quaternion: simd_quatd)
    // Monitor or KVO-observe progress toward the orientation goal.
    let progress = try dockAccessory.setOrientation(rotation, duration: .seconds(duration), relative: relative)
       // Do something with orientation progress.
    }
} catch {
    // Handle any errors.
}
```

The system tracking enabled state isn’t guaranteed to persist across reboots, app launch/termination, or background/foreground states. Enable or disable system tracking whenever your app needs the value to change.

Changes to the tracking are local to the app, and are changeable dynamically anytime during app lifecycle.

## See Also

- [Track custom objects in a frame](track-custom-objects-in-a-frame.md)
  Use your machine learning model to focus on a specific subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/modify-rotation-and-positioning-behavior-programmatically)*