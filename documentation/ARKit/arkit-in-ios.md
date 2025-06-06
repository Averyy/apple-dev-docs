# ARKit in iOS

**Framework**: ARKit

Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.

## Topics

### Essentials
- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)
  Check whether your app can use ARKit and respect user privacy at runtime.
- [USDZ schemas for AR](../RealityKit/usdz-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USDZ schemas.
### Setup
- [Choosing Which Camera Feed to Augment](choosing-which-camera-feed-to-augment.md)
  Add visual effects to the user’s environment in an AR experience through the front or rear camera.
- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)
  Keep the user informed on the current session state and recover from interruptions.
- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)
  Control rendering of your app’s virtual content on top of a camera feed.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [Configuration Objects](configuration-objects.md)
  Configure your augmented reality session to detect and track specific types of content.
### Views
- [@MainActor @objc @preconcurrency class ARView](../RealityKit/ARView.md)
  A view that enables you to display an AR experience with RealityKit.
- [class ARSCNView](arscnview.md)
  A view that blends virtual 3D content from SceneKit into your augmented reality experience.
- [class ARSKView](arskview.md)
  A view that blends virtual 2D content from SpriteKit into the 3D space of an augmented reality experience.
- [class ARCoachingOverlayView](arcoachingoverlayview.md)
  A view that displays standardized onboarding instructions to direct users toward a specific goal.
### Virtual Content
- [Content Anchors](content-anchors.md)
  Identify items in the physical environment, including planar surfaces, images, physical objects, body positions, and faces.
- [Environmental Analysis](environmental-analysis.md)
  Analyze the video from the cameras and the accompanying data, and use ray-casting and depth-map information to determine the location of items.
- [Camera, Lighting, and Effects](camera-lighting-and-effects.md)
  Determine the camera position and lighting for the current session, and apply effects, such as occlusion, to elements of the environment.
- [Data Management](data-management.md)
  Obtain detailed information about skeletal and face geometry, and saved world data.
- [Creating USD files for Apple devices](../RealityKit/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
### AR Quick Look
- [Previewing a Model with AR Quick Look](previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.
- [Adding Visual Effects in AR Quick Look and RealityKit](adding-visual-effects-in-ar-quick-look-and-realitykit.md)
  Balance the appearance and performance of your AR experiences with modeling strategies.
- [Adding an Apple Pay Button or a Custom Action in AR Quick Look](adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look.md)
  Provide a banner that users can tap to make a purchase or perform a custom action in an AR experience.
- [class ARQuickLookPreviewItem](arquicklookpreviewitem.md)
  An object for customizing the AR Quick Look experience.
- [USDZ schemas for AR](../RealityKit/usdz-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USDZ schemas.
- [Specifying a lighting environment in AR Quick Look](specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.
### Shared Experiences
- [Streaming an AR experience](streaming-an-ar-experience.md)
  Control an AR experience remotely by transferring sensor and user input over the network.
- [Creating a collaborative session](creating-a-collaborative-session.md)
  Enable nearby devices to share an AR experience by using a peer-to-peer multiuser strategy.
- [Creating a multiuser AR experience](creating-a-multiuser-ar-experience.md)
  Enable nearby devices to share an AR experience by using a host-guest multiuser strategy.
- [class ARParticipantAnchor](arparticipantanchor.md)
  An anchor for another user in multiuser augmented reality experiences.
- [ARSession.CollaborationData](arsession/collaborationdata.md)
  An object that holds information that a user has collected about the physical environment.
### Audio
- [Creating an immersive ar experience with audio](creating-an-immersive-ar-experience-with-audio.md)
  Use sound effects and environmental sound layers to create an engaging AR experience.
### Errors
- [struct ARError](arerror.md)
  An error reported by ARKit.
- [ARError.Code](arerror/code.md)
  Codes that identify errors in ARKit.

## See Also

- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)
  Check whether your app can use ARKit and respect user privacy at runtime.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [class ARAnchor](aranchor.md)
  An object that specifies the position and orientation of an item in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkit-in-ios)*