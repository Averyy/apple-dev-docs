# Migrating older projects to Reality Composer Pro 3

**Framework**: Reality Composer Pro

Bring existing Reality Composer Pro 2 projects into the Reality Composer Pro 3 workspace.

#### Overview

This article describes how to migrate a project from Reality Composer Pro 2 to Reality Composer Pro 3. It provides a brief overview of the new Reality Composer Pro 3 interface, describes key differences between Reality Composer Pro 3 and older versions, and explains what to expect before, during, and after migration.

#### Review Reality Composer Pro 3 Panels

Reality Composer Pro 2 projects contain one or more USD scenes that you edit directly from Reality Composer Pro 2. Reality Composer Pro 3, however, is not a USD editor. Scenes in Reality Composer Pro 3 consist of entities and assets. Entities are general-purpose objects that can contain any number of project assets. Assets are files stored on disk and applied to entities.

Assets can be images used for textures, audio files, materials, graphs, or animations, for example. Assets such as a Shader Graph or Script Graph, for example, can be created inside Reality Composer Pro 3. Alternatively, assets can be files created externally and then imported into your Reality Composer Pro 3 project, such as images used for textures or audio files used for sound effects . You work on Reality Composer Pro 3 Entity and Project assets through purpose-built panels, each of which is described below:

- **Project Browser**: The project-wide asset library, organized in folders. A new project starts with a core folder and a world root entity, but Reality Composer Pro 3 doesn’t create the world root entity in a migrated project.
- **Hierarchy**: The tree of entities you’re currently editing, displaying entities and components for the currently open scene.
- **Inspector**: The component editor for the currently selected entity.
- **Viewport**: The 3D project viewport for selecting and transforming entities in the currently open scene.
- **Console**: Shows import and runtime messages and errors.

> **Note**: See [`Navigating the Reality Composer Pro workspace`](realitycomposerpro-essentials-workspaceoverview.md) and [`Configuring the project workspace`](realitycomposerpro-essentials-configuringprojectworkspace.md) to learn more about navigating and customizing the Reality Composer Pro 3 Project Workspace.

#### Compare the Reality Composer Pro 3 Component System to the Usd Editor

Reality Composer Pro is a scene authoring tool for RealityKit. Projects are organized like RealityKit itself. Both Reality Composer Pro 3 and Reality Composer Pro 2 work with entities and components; however, the underlying model used to edit scenes has changed in Reality Composer Pro 3. In previous versions of Reality Composer Pro, your project was a USD scene. Everything you see in the hierarchy is a USD primitive, and you edit USD directly. When you open a  Reality Composer Pro 2 project in Reality Composer Pro 3, the USD primitives are converted into the assets, entities, and components used in Reality Composer Pro 3. Briefly:

- **Entity**: The things in your scene.
- **Component**: Gives entities behavior.
- **Asset**: What components reference, which can include meshes, materials, textures, animations, and audio, to name a few. Assets are reusable.

> **Note**: In Reality Composer Pro 3, USD is now an import and export format, not the live editing model.

The conversion process causes most of the surprises you may encounter after migrating projects from earlier versions of Reality Composer Pro. Some primitives map cleanly to the Reality Composer Pro 3 ECS format. Others only map partially. A small number of Reality Composer Pro 2 primitives don’t map to a direct counterpart in Reality Composer Pro 3 and will need to be rebuilt by hand. See [`Updating migrated assets to Reality Composer Pro 3`](realitycomposerpro-essentials-updating-migrated-assets-to-reality-composer-pro-3.md) for more information.

#### Migrate Custom Components As Placeholders

When you first migrate project from a previous version of Reality Composer Pro, Reality Composer Pro 3 preserves all custom component data in a placeholder format.

Connect the Reality Composer Pro 3 project to the Xcode project containing the plugin that implements the custom components. Reality Composer Pro 3 then uses the Swift definitions to update these placeholders with definitions linked to the plugin implementation. See [`Link your migrated project to Xcode`](realitycomposerpro-essentials-migrating-older-projects-to-reality-composer-pro-3#Link-your-migrated-project-to-Xcode.md) later in this article for more information.

As long as the Swift definitions haven’t changed since you used them to create the project being migrated, this transition occurs seamlessly when you connect the Xcode project. Reality Composer Pro 3 propagates subsequent changes to the Swift definitions to the Reality Composer Pro 3 custom components whenever you reload the plugin.

#### Optionally Adopt Live Component Editing in Reality Composer Pro 3

Your custom component code from your migrated project continues to work without changes when you run your Xcode project on a device or simulator — the experience is the same as before, and this step is entirely optional. Optionally, in Reality Composer Pro 3 you can also run your custom component directly in the Viewport and edit its parameters in real time. To adopt this experience, import the [`Reality Composer Pro Plugin`](https://developer.apple.comhttps://github.com/apple/reality-composer-pro-plugin) Swift package, conform to the `RealityComposerProPlugin` protocol, and register your custom systems.

#### Work with Reality Composer Pro 3 Independently of Xcode

In Reality Composer Pro 2, Reality Composer Pro content lives inside your Xcode project as the `RealityKitContent` Swift package created by the visionOS app template. You edit your app and its content in the same workspace. Starting with the 2026 releases, Reality Composer Pro 3 is a standalone app. Your Reality Composer Pro project is no longer part of your Xcode project, so the workflow has changed. Key things to know about how this changes your workflow:

- Linking an Xcode project to Reality Composer Pro 3 requires Xcode 27 or later.
- Reality Composer Pro 3 is a standalone app and independent of any Xcode project. Xcode now consumes your content instead of containing it.
- Your app uses exported `.reality` files. Unlike Reality Composer Pro 2, editing the `RealityKitContent` package no longer updates your app — exporting is now an explicit build step.
- [Optional] Migrate any custom code you want to keep from the `RealityKitContent` package into your app or another dedicated Swift package. Reality Composer Pro 3 migrates your assets but doesn’t migrate custom Swift code. The existing Xcode project continues to work properly with the custom code in the Swift package. With Reality Composer Pro 3, the custom code does not need to live in a Swift package that contains the `.realitycomposerpro` project, but it can.
- Reality Composer Pro 3 stores the Xcode link as a file path. If you move or rename the `.xcodeproj`, or open it on another Mac where the path is different, Reality Composer Pro 3 treats the project as unlinked and prompts you to link it again.

To export a scene or entity from Reality Composer Pro 3, Control-click it in the Project Browser and then choose Export To > Reality. Save the exported `.reality` file in your Xcode project; Xcode automatically detects the file, and you can load it at runtime from a [`RealityView`](https://developer.apple.com/documentation/realitykit/realityview).

For faster iteration, link an Xcode project instead. After linking, you can edit your scene and run your app in Simulator or on a device directly from the Play button in the Launch Control bar. To create the link, choose Run with Xcode and select an existing project, or create a new one. See [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md) to learn more.

> ❗ **Important**: - Direct USD export (mesh) is available only in Reality Composer Pro 3 and later.
- Because Reality Composer Pro 3 isn’t a USD editor, exporting from it rebuilds a fresh USD stage rather than round-tripping the original. Exporting doesn’t preserve hand-authored layer structures, references, payloads, comments, primitive ordering, or many names.

#### Migrate a Reality Composer Pro 2 Project

When you open an older project, Reality Composer Pro 3 detects the legacy package and prompts you to migrate. Migrating an older project is one way but does not modify or write to the original `.realitycomposerpro` project. Reality Composer Pro 3 names the new project after the old Swift package, not the folder you clicked, and the project has no default save location until after you save it.

The project file format is also different. A Reality Composer Pro 3 project is a `.realitycomposerpro` bundle, and its state lives in this store rather than in loose USD files on disk as in older versions. Organizational Scope primitives disappear during migration.

Reality Composer Pro 2 commonly uses USD Scope nodes just to group things, but because the Reality Composer Pro 3 ECS has no equivalent, Reality Composer Pro 3 doesn’t recreate Scopes. Instead, it reparents their children. Your imported project may look flatter than the original.

1. Open Finder, locate and then open the Reality Composer Pro 2 package. Alternatively, Control-click the RCP2 package and then choose Open With > Reality Composer Pro 3.
2. Click Allow (if prompted) to give RCP3 folder access permissions and then click Migrate.
3. If the message “Unsupported Actions Detected” appears, click OK. See [`Review migrated Sequences and rebuild actions`](realitycomposerpro-essentials-updating-migrated-assets-to-reality-composer-pro-3#Review-migrated-Sequences-and-rebuild-actions.md) for more information about reviewing migrated sequences and rebuilding actions.
4. Reality Composer Pro 3 imports assets from the `RealityKitContent.rkassets` into the Project folder and shows them in the Project Browser. Reality Composer Pro 3 places imported entities at the root of the Project folder and places related supporting assets (such as textures, geometry, animations, and materials) into subfolders of each imported entity.

![A screenshot of the RCP3 Project Browser showing an asset and subfolders after importing an RCP2 project into RCP3.](/images/RealityComposerPro/RCP3Migration@2x.png)

#### Link Your Migrated Project to Xcode

After migrating your RCP2 project to RCP3, you may need to re-link it to its associated Xcode project.

1. In the Launch Control bar, switch from Simulate to Run with Xcode.
2. In the Launch Control bar, next to Run with Xcode, choose Link an Xcode project.
3. Click Link Existing Project, then locate the project and click Link Project. See [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md) to learn more.

#### Use Xcode 27 or Later to Use Assets in the Reality File

After migration, your Xcode project still has the older Reality Composer Pro 2 package in it, and any remaining Swift files still point to the older `RealityKitContent` bundle.

| `RealityKitContent` | During Migration | After Migration |
| --- | --- | --- |
| `.realitycomposerpro` project | RCP3 imports this | No actions necessary |
| `.rkassets` asset bundle | RCP3 supersedes this with your new project | You can potentially remove this after migration. RCP3 fully imports the contents of the `.rkassets` folder into the project, making it self-contained, but RCP3 could still re-import them if they change. For example, if an artist updates existing assets using a digital content creation (DCC) tool, removing the `.rkassets` folder would break that link and interrupt existing workflows for updating project assets. |
| Custom Swift Code | RCP3 doesn’t migrate this automatically | Optionally, if you moved your custom code from the `RealityKitContent` package and don’t have any dependency on it, you can delete the package and update any code that still references it. Link your Xcode project in RCP3 using the Run with Xcode option. |

See [`Updating migrated assets to Reality Composer Pro 3`](realitycomposerpro-essentials-updating-migrated-assets-to-reality-composer-pro-3.md) for more information.

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Updating migrated assets to Reality Composer Pro 3](realitycomposerpro-essentials-updating-migrated-assets-to-reality-composer-pro-3.md)
  Fix common problems that appear after migrating a project from Reality Composer Pro 2 to Reality Composer Pro 3.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-migrating-older-projects-to-reality-composer-pro-3)*