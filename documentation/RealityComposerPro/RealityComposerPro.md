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
  Explore the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.
### Materials
- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties to 3D entities to control how they look in your scene.
- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Assign and configure surface materials on 3D model assets in Reality Composer Pro.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.
### Particle Emitter
- [Creating particle systems in Reality Composer Pro](creating-particle-systems-in-reality-composer-pro.md)
  Add Particle Emitters and Particles to scenes to create nearly any type of visual effect.
### Script Graph
- [Getting started with Script Graphs](getting-started-with-script-graphs.md)
  Build interactive, code-free 3D experiences using a visual, node-based editor in Reality Composer Pro.
### Compute Graph
- [Introducing Compute Graph](introducing-compute-graph.md)
  Use Reality Composer Pro Compute Graph to build custom particle simulations with a node-based graph.
- [Building a working Compute Graph example](building-a-working-compute-graph-example.md)
  Combine emission, initialization, simulation, and output nodes into a falling-snow effect colored from a gradient texture.
### Animation
- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Automating motion path creation with editor-scripting commands](automating-motion-path-creation-with-editor-scripting-commands.md)
  Build the same multi-track Sequence and Motion Path shown in the Sequencer UI programmatically, by chaining editor-scripting commands together.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.
### Assistant
- [Working with the Reality Composer Pro Assistant](working-with-the-reality-composer-pro-assistant.md)
  Connect an AI model to Reality Composer Pro to generate assets and get contextual help building scenes.
### Audio
- [Adding audio components in Reality Composer Pro](introduction-to-reality-composer-pro-audio.md)
  Configure audio components in a Reality Composer Pro scene.
- [Optimizing audio playback in Reality Composer Pro](optimizing-audio-playback.md)
  Balance audio quality against CPU, memory, and power cost when configuring playback.
### Release notes
- [Reality Composer Pro Release Notes](reality-composer-pro-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 2 Release Notes](reality-composer-pro-beta-2-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 3 Release Notes](reality-composer-pro-beta-3-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.
- [Reality Composer Pro Beta 4 Release Notes](reality-composer-pro-beta-4-release-notes.md)
  Review known issues and changes in Reality Composer Pro 3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityComposerPro)*