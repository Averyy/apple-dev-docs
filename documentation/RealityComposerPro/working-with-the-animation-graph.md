# Working with the Animation Graph

**Framework**: Reality Composer Pro

Define and control character animations using a visual, node-based state machine in Reality Composer Pro.

#### Overview

Use animation graphs to create custom animations in a visual, node-based, code-free workflow. Using the Animation Graph, you can create tags and conditions to control the flow between different animation states.

![Screenshot of animation graph](https://docs-assets.developer.apple.com/published/02e03d4d0cfb29d97c07839d0be1bf0f/AnimationGraph%402x.png)

##### Before You Begin

For general navigation and features in the Graph Editor, see [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

##### Create an Animation Graph

1. In the Project Browser, right-click a folder and then click **New** > **Animation Graph.**
2. Enter a name for the Animation Graph, and then double-click it to open it in the Animation Graph Editor.
3. In the Inspector, click **Skeleton Definition** to browse to and select the skeleton definition you want to use. For imported entities, Reality Composer Pro creates the skeleton definition when you import the entity. It includes all dependencies, such as blend masks and inverse kinematic rigs.
4. In the Inspector, select a **Preview Entity**. This is the entity shown in the preview window. Changing this option allows you to preview your animations for different entities that share the same skeleton definition.

##### Add Animation Graph Inputs

Inputs provide a variety of parameters that can control the animation that plays at runtime. For example, an Input parameter named Jump can trigger a jumping animation.

##### Add an Input

1. In the Inspector, under **Inputs** click **[+]** to add an input.
2. Pick an **Input Parameter** type: - Bool Parameter
- Float Parameter
- Int Parameter
- Option Parameter
- Rotation Parameter
- Skeletal Pose Parameter
- Trigger Parameter
- Vector Parameter
3. Click the name to update the parameter name (if needed).
4. Set the **Default Value** (if needed) and **Read Only** toggle if needed.

![Screenshot of adding an input modal](https://docs-assets.developer.apple.com/published/8523c70ed70d87d6d624a01f24f25e07/AddInput%402x.png)

##### Add and Configure a State Machine Node

1. In your animation graph, press N (or spacebar) and then select the **State Machine** node.
2. Double-click the **State Machine** node. This opens an empty space inside the node where you can add tags and conduits.
3. Control-click anywhere in the empty space and then click **Add State**.
4. In the Inspector, click in the **Name** field and give your state a name.
5. Enable the appropriate toggle(s) for your state: **Start State**, **End State**, or  **Pass Through**.
6. Next to **Tags,** click [+] to add a tag to your state.
7. Click in the Tag field and then select a tag from the list.
8. Click in the field next to the tag, and then select one of the following options: - **On Enter** — Tag is activated when the entity enters the specified state.
- **On Exit** —  Tag is activated when the entity exits the specified state.
- **On Enter and Exit** —  Tag is activated when the entity enters the state and when the entity exits the state.
- **While Active** — Tag is activated as long as the entity remains in the specified state.

![Screenshot of adding a tag modal](https://docs-assets.developer.apple.com/published/07cac85823be9dbadd0f96202e23b157/Conditions%402x.png)

> 💡 **Tip**: When editing a State Machine, click a State to view or change its associated tags and properties.

##### Use Animation Graph Tags

You attach tags to different animation states (using a State Machine node) and use them as triggers (conditions) to change animation states. For example, you can create a tag for when a specific animation state is active for an entity. Then you can use that tag to control the animation state.

Example:

- If an entity is currently in an active state called  “CarryingHeavyObject”, then the current state could be tagged with “HeavilyEncumbered”.
- When the “Heavily Encumbered” tag = true, you can trigger a different animation state.

You activate tags based on the same options described in the State Machine section above: On Enter, On Exit, On Enter and Exit, and While Active.

##### Add an Animation Graph Tag

1. In the Inspector panel, in the **Tags** section, click **[+]** Add Tag.
2. Select **Type** of tag: 1. Internal
2. Play Audio
3. Enable/Disable Entity tag
3. Click the name to enter a new name for the tag.

![Screenshot of adding a tag modal](https://docs-assets.developer.apple.com/published/34cd56134bf0e32faef4e07d62620b65/AddTag%402x.png)

##### Edit or Delete Animation Graph Tags

- **Edit an existing tag**: To edit a tag, click it, and then edit the properties.
- **Delete a tag**: Click the tag to select it, and then click **[-].**

##### Connect and Configure Conduits Between States

Click on the edge of a state and then drag the arrow to another state.

##### Add a Condition to a Conduit Between States

![Screenshot of context menu addition a condition](https://docs-assets.developer.apple.com/published/f3a3b52a4fa8532b5f678cb9b88c34bc/Transitions%402x.png)

1. Control-click anywhere in the empty space and then click **Add Conduit**. A conduit is a transition state that lets you route multiple states through a shared condition, so you define the condition once rather than repeating it on each state-to-state transition. A conduit can also branch to multiple different destination states.
2. Click on the edge of added conduit, and then drag an arrow to a State.
3. Control-click the conduit connector, click **Add Condition**, and then select a condition (Bool, Finished, Float, and so on).

![Screenshot of context menu addition a condition](https://docs-assets.developer.apple.com/published/45bdd5cbb570a189ce3a0390c90be7ca/AddCondition%402x.png)

1. In the Inspector, under **Conditions**, configure your condition. Click the operator icon to change the operator (==, !=, and so on).
2. Click **Settings** to set Compare to Value or Compare to Parameter.

> 💡 **Tip**: The editor displays different conditions in different colors — for example, trigger conditions appear as blue, while boolean conditions appear as green.

##### Preview Your Animation

In the Animation Graph, at the top of the screen, click **Debug Graph** and then click **Play**.

This allows you to preview how your animations appear and watch the visual flow between nodes (indicated by animated connectors in the Animation Graph) as the entity enters and exits states.

In addition, in the Inspector panel Tags section, you can watch tags activate and deactivate (indicated by the pulsing dots next to the tag names) as your animation plays.

![Screenshot activating the debug menu](https://docs-assets.developer.apple.com/published/0b9794b972b7a6897b6098b43cd69ab7/DebugGraph%402x.png)

##### Apply an Animation Graph to an Entity

To apply your animation graph to an entity:

1. In the Scene Hierarchy, click on an entity.
2. In the Inspector, click **Add Component**, and then click **Animation Graph.**
3. Click in the **Animation Graph** field, and then select the Animation Graph you want to apply from the pop-up menu.

![Screenshot of the animation graph component](https://docs-assets.developer.apple.com/published/dc356a2e7374bcc76c9db96fbf90513c/AnimGraphComponent%402x.png)

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build and customize animation sequences to control entity movement and behavior in your scene.
- [Building a navmesh in Reality Composer Pro](building-a-navmesh-in-reality-composer-pro.md)
  Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/working-with-the-animation-graph)*