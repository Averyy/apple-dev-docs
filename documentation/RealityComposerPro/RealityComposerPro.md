# Reality Composer Pro

**Framework**: Reality Composer Pro

Build, design, and orchestrate 3D content for your RealityKit apps.

#### Overview

Reality Composer Pro 3 makes it easy to rapidly iterate, preview, and prepare 3D content for your visionOS apps, iOS apps, and more — right on your Mac. Build stunning scenes and animate characters with cinematic precision. And you can preview your changes live on Apple Vision Pro.

![A screenshot of Reality Composer Pro.](https://docs-assets.developer.apple.com/published/6358581971f04ea168a3a38d38f011ab/Overview%402x.png)

Reality Composer Pro includes editors and workflows for designing materials with Shader Graph, building visual scripts with Script Graph, authoring GPU-driven simulations with Compute Graph, defining character behaviors with Animation Graphs, and editing skeletons.

##### System Requirements

- macOS Tahoe 26.5 or later

##### Entities Components and Systems

Reality Composer Pro is a 3D content creation platform backed by an **Entity Component System (ECS)**. Reality Composer Pro is built around the ECS pattern, so a basic understanding of ECS provides helpful context.

The ECS model has three building blocks: entities, components, and systems.

- **Entities** are general-purpose objects. An entity can represent any object in your project, such as a vehicle, a mountain, or a character.
- **Components** are the building blocks that define and control every aspect of an entity, such as animations, materials, behaviors, visual effects, and audio. Components contain the data needed to model each aspect, and they add to and update systems. For example, every damageable object in a game has a health component.
- **Systems** define a process that acts on every entity with the required components. For example, a physics system queries entities that have mass, velocity, and position components, then uses that data to perform calculations for each entity. Systems act globally over all entities with the required components — entities that lack the components, such as a tree or a chair, are ignored.

Systems change an entity’s behavior at runtime by adding, removing, or modifying components.

> **Note**: To learn more about RealityKit components, see [`Understanding the modular architecture of RealityKit`](https://developer.apple.com/documentation/visionOS/understanding-the-realitykit-modular-architecture).

##### Whats New in Reality Composer Pro

This release of Reality Composer Pro is a complete 3D development platform. The previous version focused on authoring spatial content for Apple Vision Pro; this release adds new features and functionality, such as:

- Character intelligence and AI behaviors
- A new in-editor lightmap baker
- A new Compute Graph for authoring GPU-driven simulations for visual effects, such as particles
- Animation Graphs to define character behaviors (for example, Idle, Run, Jump)
- Script Graph for visual scripting directly inside the tool
- A new Skeleton Editor
- Generative AI capabilities in a UI Assist layer, including a Help Agent, Prototyping Agent, and Asset Generation tools
- A new and improved Live Preview on Device
- Physics

> ❗ **Important**: This release fully deprecates and removes the previous version of Reality Composer Pro.

## Topics

### Essentials
- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.
### Materials
- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties such as color, roughness, and transparency to 3D entities in your scene.
- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Work with materials in Reality Composer Pro to enhance the appearance of your model.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.
### Script graph
- [Getting started with script graphs](getting-started-with-script-graphs.md)
  Build interactive, code-free 3D experiences using the visual node-based script graph editor.
### Character Intelligence
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.
### Animation
- [Creating animation sequences](creating-animation-sequences.md)
  Build and customize animation sequences to control entity movement and behavior in your scene.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Define and control character animations using a visual, node-based state machine in Reality Composer Pro.
### Assistant
- [Working with the Reality Composer Pro assistant](working-with-the-reality-composer-pro-assistant.md)
  Connect an AI model to Reality Composer Pro to generate assets, organize scenes, and get feature guidance.
### Release notes
- [Reality Composer Pro Release Notes](reality-composer-pro-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityComposerPro)*