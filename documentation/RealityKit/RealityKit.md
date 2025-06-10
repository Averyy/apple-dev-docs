# RealityKit

**Framework**: RealityKit  
**Kind**: module

Simulate and render 3D content for use in your augmented reality apps.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Mentions

- [Selecting an anchor for a Reality Composer scene](selecting-an-anchor-for-a-reality-composer-scene.md)
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
- [Configuring elements in a scene](configuring-elements-in-a-scene.md)
- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)

#### Overview

RealityKit provides high-performance 3D simulation and rendering capabilities you can use to create apps with 3D or augmented reality (AR) for iOS, iPadOS, macOS, tvOS, and visionOS. RealityKit is an AR-first 3D framework that leverages [`ARKit`](https://developer.apple.com/documentation/ARKit) to seamlessly integrate virtual objects into the real world.

![A screenshot that shows a virtual warehouse environment set up as a theater. A movie showing on a big floating screen features a wheeled robot rolling through an outdoor environment.](https://docs-assets.developer.apple.com/published/608fdec903f17a98916147458196a26f/realityKit-hero-image.png)

Use RealityKit’s rich functionality to create compelling augmented reality (AR) experiences:

- Create and import full RealityKit scenes with models, animations, and Spatial Audio by using Reality Composer Pro for visionOS.
- Build or modify scenes at runtime by adding 3D models, shape primitives, and sounds from code.
- Have virtual objects interact with objects in the real world.
- Animate objects, both manually and with physics simulations.
- Respond to user input and changes in a person’s surroundings.
- Synchronize across devices and use SharePlay to enable group AR experiences.

## Topics

### Essentials
- [Understanding the modular architecture of RealityKit](../visionOS/understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Building an immersive experience with RealityKit](building-an-immersive-experience-with-realitykit.md)
  Use systems and postprocessing effects to create a realistic underwater scene.
- [class Entity](entity.md)
  An element of a RealityKit scene to which you attach components that provide appearance and behavior characteristics for the entity.
- [protocol Component](component.md)
  A representation of a geometry or a behavior that you apply to an entity.
### Presentation
- [Views and attachments](presentation-views-and-attachments.md)
  Bring RealityKit content into your app with views and renderers.
- [Presentation UI](presentation-user-interface.md)
  Control your app’s content and how people can interact with it.
### Scene management and logic
- [Scenes](ecs-scenes.md)
  The context that holds all RealityKit entities.
- [Systems](ecs-systems.md)
  Apply behaviors and physical effects to the entities in a RealityKit scene.
- [Events](ecs-events.md)
  Respond to things happening in your RealityKit scene by subscribing to specific event types.
- [Entity actions](ecs-entity-actions.md)
  Create simple, reusable actions that can change your app state, RealityKit scene, or animate an entity.
### Asset creation
- [Designing RealityKit content with Reality Composer Pro](../visionOS/designing-realitykit-content-with-reality-composer-pro.md)
  Design RealityKit scenes for your visionOS app.
- [Swift Splash](../visionOS/swift-splash.md)
  Use RealityKit to create an interactive ride in visionOS.
- [Diorama](../visionOS/diorama.md)
  Design scenes for your visionOS app using Reality Composer Pro.
- [Composing interactive 3D content with RealityKit and Reality Composer Pro](composing-interactive-3d-content-with-realitykit-and-reality-composer-pro.md)
  Build an interactive scene using an animation timeline.
- [Presenting an artist’s scene](presenting-an-artists-scene.md)
  Display a scene from Reality Composer Pro in visionOS.
- [Reality Composer](realitykit-reality-composer.md)
  A visual editor for RealityKit AR scenes.
- [Object capture](realitykit-object-capture.md)
  Create 3D objects from a series of photographs using photogrammetry.
- [USD Assets](realitykit-usd-assets.md)
  Import and use 3D scenes by importing USD files.
### Scene content
- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](../visionOS/enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Presenting images in RealityKit](presenting-images-in-realitykit.md)
  Create and display spatial scenes in RealityKit.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Anchors](scene-content-anchors.md)
  Lock virtual content to the real world.
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.
### Game development
- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](game-development-character-skeletons.md)
  Direct the movements and animation of models.
### Physics simulation
- [Collision detection](physics-collision-detection.md)
  Determine when entities collide with each other or the environment.
- [Simulations and motion](physics-simulations-and-motion.md)
  Simulate physical interactions between entities or systems.
- [Force effects](physics-force-effects.md)
  Control the movement of virtual objects with forces.
- [Physics joints and pins](physics-joints-and-pins.md)
  Simulate joint physics that connect virtual objects.
### Performance improvements
- [Improving the Performance of a RealityKit App](improving-the-performance-of-a-realitykit-app.md)
  Measure CPU and GPU utilization to find ways to improve your app’s performance.
- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)
  Prevent the GPU from limiting your app’s frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
  Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](construct-an-immersive-environment-for-visionos.md)
  Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](passing-metal-command-objects-around-your-application.md)
  Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.
- [protocol Resource](resource.md)
  A shared resource you use to configure a component, like a material, mesh, or texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit)*