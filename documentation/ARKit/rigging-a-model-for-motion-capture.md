# Rigging a Model for Motion Capture

**Framework**: ARKit

Configure custom 3D models so ARKit’s human body-tracking feature can control them.

#### Overview

ARKit recognizes and tracks a person’s movements using an iOS device’s rear camera. RealityKit applies the detected motion to a 3D character model in real time, allowing the person on camera to control the movement of the 3D model, much like a virtual puppet. You can try out this feature by downloading sample code in [`Capturing Body Motion in 3D`](capturing-body-motion-in-3d.md).

##### Configure Your Model

You can configure your own models so RealityKit’s puppeteering functionality can control them. Your character model must be a skeletal mesh exported as a USDZ file and must conform to a specific joint hierarchy and naming convention. Models that don’t conform may behave unexpectedly or fail to work at all. Learn more about the specific joint hierarchy and required names for puppeteering models at [`Validating a Model for Motion Capture`](validating-a-model-for-motion-capture.md).

##### Download the Robot Model

The easiest way to configure your model for puppeteering is to rig it to the skeleton from the robot model in the [`Capturing Body Motion in 3D`](capturing-body-motion-in-3d.md) sample. By using the robot model’s skeleton to rig your own model, you’ll start with the correct bone names and hierarchy. You can download a zip file containing both the USDZ and FBX versions of the [`robot character`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/Biped-Robot.zip).

> **Note**:  If you already have a rigged humanoid model and prefer to modify your existing skeleton to match [`RealityKit`](https://developer.apple.com/documentation/RealityKit)‘s expected format instead of rebinding your model to the provided skeleton, you can find detailed information on the joint names and hierarchy required by ARKit’s motion capture functionality in [`Validating a Model for Motion Capture`](validating-a-model-for-motion-capture.md).

 If you already have a rigged humanoid model and prefer to modify your existing skeleton to match [`RealityKit`](https://developer.apple.com/documentation/RealityKit)‘s expected format instead of rebinding your model to the provided skeleton, you can find detailed information on the joint names and hierarchy required by ARKit’s motion capture functionality in [`Validating a Model for Motion Capture`](validating-a-model-for-motion-capture.md).

##### Import the Skeleton Into Your 3d Modeling Program

In your 3D-modeling software package (such as Maya, Cinema4D, or Modo), import the provided skeleton and the custom mesh model that you want to use with ARKit’s Motion Capture functionality. You should model your mesh in a standard T-pose.

It’s very important that you configure your import settings so that they don’t change the orientation of the imported character or any of the skeleton’s individual joints. After import, the character should be oriented facing the +Z axis, with the top of its head oriented toward the +Y axis, and the character’s left hand pointing along the +X axis. Your scene should also be configured with +Y as the up axis. In some software packages, this orientation requires changing the default scene configuration.

![Illustration of two human-shaped robots, one facing forward in T-pose and the other in profile. For both images, the correct orientation is indicated with a right angle graph in which +Y represents up, +Z represents forward, and +X represents the character’s left.](https://docs-assets.developer.apple.com/published/a7a7f0c74c8b284ad33dbb3ccdbfb7a4/media-3588329%402x.png)

> **Note**:  Some 3D software packages predefine which axis runs the length of the bone. You may not be able to export a compatible model from these programs without additional scripting or conversion work.

 Some 3D software packages predefine which axis runs the length of the bone. You may not be able to export a compatible model from these programs without additional scripting or conversion work.

Once you’ve imported the robot character file, unbind and delete the robot mesh. You only need the skeleton from the imported file, since you’ll be binding your own mesh to it. Make sure you don’t change the joint names or relationships, and hang your custom geometry to the same node as the he skeleton and your custom geometry must be parented in separate hierarchies in order to export a valid USDZ for puppeteering. There should be no geometry descending from joints, and no joints descending from geometry.

##### Match the T Pose Rest Position

Next, align your mesh to the imported skeleton, then scale, translate, and rotate it until it matches the imported skeleton as closely as you can get it. Finally, freeze transformations on the mesh.

![Illustration showing a character in a T-pose configuration.](https://docs-assets.developer.apple.com/published/8374dd9a42cebd94032883bdf6651811/media-3588331%402x.png)

Finish matching the mesh and armature by moving any joints of the armature that don’t line up correctly with the mesh, making sure that the X axis still points down the length of the bone after you’re done moving it. Many 3D software packages include tools to automatically re-orient joints based on the location of their children. If a re-orienting feature is available in your software package, use it when you’re done moving joints into new locations.

> ❗ **Important**:  The Motion Capture feature doesn’t retarget motion before applying it to your model. If your custom character’s proportions differ substantially from the provided skeleton, the puppeteering functionality may not perform as expected unless you adjust for the differences in your own code.

 The Motion Capture feature doesn’t retarget motion before applying it to your model. If your custom character’s proportions differ substantially from the provided skeleton, the puppeteering functionality may not perform as expected unless you adjust for the differences in your own code.

##### Bind Your Mesh to the Imported Skeleton

Once you’ve aligned your mesh with the skeleton, bind your mesh to it. For best performance, you should use no more than four skin influences per vertex. You character should be modeled in a T-pose, your scene should contain only one bind pose, and the rotational values of each joint in your hierarchy should match the values in the provided example skeleton.

##### Export the Model

After you’ve tested your bound mesh and are happy with your vertex weights and joint deformations, export your model to a USDZ file. If your 3D package doesn’t support exporting directly to USDZ, you can export as a GLTF or USD file and then use Reality Converter to convert that file to USDZ. Reality Converter will also convert FBX files if you manually install the Autodesk FBX Python SDK available from Autodesk’s website.

Xcode automatically configures USDZ files imported into an AR application target and adds them to your app bundle when building so they become available to load at runtime.

For more information on loading and using the model once it’s in your Xcode project, see the [`Capturing Body Motion in 3D`](capturing-body-motion-in-3d.md) sample code project, which demonstrates how to load and display a skeletal model contained in a USDZ file as a [`BodyTrackedEntity`](https://developer.apple.com/documentation/RealityKit/BodyTrackedEntity).

## See Also

- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [Validating a Model for Motion Capture](validating-a-model-for-motion-capture.md)
  Verify that your character model matches ARKit’s Motion Capture requirements.
- [class ARBodyAnchor](arbodyanchor.md)
  An anchor that tracks the position and movement of a human body in the rear-facing camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/rigging-a-model-for-motion-capture)*