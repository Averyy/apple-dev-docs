# GKAgent

**Framework**: GameplayKit  
**Kind**: class

A component that moves a game entity according to a set of goals and realistic constraints.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKAgent
```

#### Overview

The [`GKAgent`](gkagent.md) class is abstract, defining only the general functionality of an agent—its movement constraints and the [`behavior`](gkagent/behavior.md) property containing its goals ([`GKGoal`](gkgoal.md) objects). To implement agent-based gameplay, choose a concrete subclass that fits your game.

- Use the [`GKAgent2D`](gkagent2d.md) class for 2D game worlds, or for 3D games where all gameplay-relevant movement is constrained to two dimensions.
- Use the [`GKAgent3D`](gkagent3d.md) class for game worlds that allow movement in three dimensions.

To learn more about the agent simulation, see [`Agents, Goals, and Behaviors`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Agent.html#//apple_ref/doc/uid/TP40015172-CH8) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

##### An Agent Is a Component

Because [`GKAgent`](gkagent.md) is a subclass of [`GKComponent`](gkcomponent.md), you can use Entity-Component architecture to add agent-based behaviors to your game. (For details on this architecture, see [`Entities and Components`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/EntityComponent.html#//apple_ref/doc/uid/TP40015172-CH6) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).)

To integrate agents with gameplay, call each agent’s [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method each time you want to update the simulation that governs the agent’s behavior. Typically, you call this method once for each frame processed by your game’s graphics engine—for example, in the [`update(_:)`](https://developer.apple.com/documentation/SpriteKit/SKScene/update(_:)) method of a SpriteKit scene or the [`renderer(_:updateAtTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:updateAtTime:)) method of a SceneKit renderer delegate. If your game uses Entity-Component architecture, you can use a [`GKComponentSystem`](gkcomponentsystem.md) object to update all the agents in the game scene for each frame. If not, you must call each agent’s [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method directly.

##### An Agent Simulates Movement Based on Goals

Each time an agent’s [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method runs, the agent evaluates each [`GKGoal`](gkgoal.md) object listed in its [`behavior`](gkagent/behavior.md) property to find the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the time delta and the agent’s maximum speed and turn rate). It then combines the effects from all the goals in its behavior, using the weights specified in the [`GKBehavior`](gkbehavior.md) object to modulate the influence of each goal, resulting in a total change in its direction and speed.

There are two options for using the output of this simulation to move game entities:

- In a per-frame update that executes after the agent’s [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method—such as the [`update(deltaTime:)`](gkcomponent/update(deltatime:).md) method of another [`GKComponent`](gkcomponent.md) subclass in your game or a game engine method such as [`didEvaluateActions()`](https://developer.apple.com/documentation/SpriteKit/SKScene/didEvaluateActions()) (SpriteKit) or [`renderer(_:willRenderScene:atTime:)`](https://developer.apple.com/documentation/SceneKit/SCNSceneRendererDelegate/renderer(_:willRenderScene:atTime:)) (SceneKit)—examine the position and rotation of each agent and use that information to update the properties of any visual objects representing the agents.
- Set the [`delegate`](gkagent/delegate.md) property of each agent to an object responsible for that agent’s visual representation. That object can implement the [`agentDidUpdate(_:)`](gkagentdelegate/agentdidupdate(_:).md) method, which the agent calls every time it updates its position and direction. In that method, you can examine the agent’s properties and make corresponding changes to a visual representation.

In addition, an agent delegate can implement the [`agentWillUpdate(_:)`](gkagentdelegate/agentwillupdate(_:).md) method to feed information into the agent simulation. This option can be useful for combining agent-based movement with an external physics engine (such as those found in SceneKit and SpriteKit), or with other APIs that might apply motion to an agent’s visual representation (such as SpriteKit actions). However, the agent simulation cannot account for momentum introduced by such influences, so the accuracy of the agent’s planning will be reduced in these scenarios.

> 💡 **Tip**:  If you use the [`GKSKNodeComponent`](gksknodecomponent.md) class to manage the relationship between an entity and a SpriteKit node,  set your [`GKSKNodeComponent`](gksknodecomponent.md) instance as the delegate for that entity’s agent, and GameplayKit will automatically synchronize the agent and its SpriteKit representation.

> **Note**:  The simulation responsible for agent movement is based on realistic physical behaviors; however, this simulation is  connected to the physics subsystems in SpriteKit, SceneKit, or any other graphics engine. For example, setting the [`mass`](gkagent/mass.md) property of an agent does not affect the collision behavior of any SpriteKit physics bodies.

## Topics

### Defining an Agent’s Behavior
- [var behavior: GKBehavior?](gkagent/behavior.md)
  A weighted collection of goals that influence the agent’s movement.
### Constraining an Agent’s Movement
- [var mass: Float](gkagent/mass.md)
  The resistance of the agent to changes in speed or direction.
- [var maxAcceleration: Float](gkagent/maxacceleration.md)
  The upper limit to changes in the agent’s speed or direction.
- [var maxSpeed: Float](gkagent/maxspeed.md)
  The agent’s maximum forward speed, in units per second.
- [var radius: Float](gkagent/radius.md)
  The agent’s radius.
### Synchronizing an Agent’s Visual Representation
- [var delegate: (any GKAgentDelegate)?](gkagent/delegate.md)
  An object that prepares for or responds to updates in the agent simulation.
### Managing an Agent’s Attributes
- [var speed: Float](gkagent/speed.md)
  The agent’s current forward speed, in units per second.

## Relationships

### Inherits From
- [GKComponent](gkcomponent.md)
### Inherited By
- [GKAgent2D](gkagent2d.md)
- [GKAgent3D](gkagent3d.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKAgent2D](gkagent2d.md)
  An agent that operates in a two-dimensional space.
- [class GKAgent3D](gkagent3d.md)
  An agent that operates in a three-dimensional space.
- [class GKGoal](gkgoal.md)
  An influence that motivates the movement of one or more agents.
- [class GKBehavior](gkbehavior.md)
  A set of goals that together influence the movement of an agent.
- [class GKCompositeBehavior](gkcompositebehavior.md)
  A set of behaviors, each of which is a set of goals, that together influence the movement of an agent.
- [class GKPath](gkpath.md)
  A polygonal path that can be followed by an agent.
- [protocol GKAgentDelegate](gkagentdelegate.md)
  Implement this protocol to synchronize the state of an agent with its visual representation in your game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent)*