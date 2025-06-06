# GameplayKit

**Framework**: GameplayKit  
**Kind**: module

Architect and organize your game logic. Incorporate common gameplay behaviors such as random number generation, artificial intelligence, pathfinding, and agent behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

GameplayKit is an object-oriented framework that provides foundational tools and technologies for building games. GameplayKit includes tools for designing games with functional, reusable architecture, as well as technologies for building and enhancing gameplay features such as character movement and opponent behavior.

##### Getting Started with Gameplaykit

GameplayKit covers many aspects of game design and development. For deeper discussions of the game design patterns you can leverage with GameplayKit, along with tutorials that illustrate building games with GameplayKit features, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

##### Related Sample Code

To experiment with GameplayKit in action, see these sample code projects:

- [`Boxes: GameplayKit Entity-Component Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016459)
- [`Dispenser: GameplayKit State Machine Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016460)
- [`Pathfinder: GameplayKit Pathfinding Basics`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/Pathfinder_GameplayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016461)
- [`AgentsCatalog: Using the Agents System in GameplayKit`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/AgentsCatalog/Introduction/Intro.html#//apple_ref/doc/uid/TP40016141)
- [`FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/FourInARow/Introduction/Intro.html#//apple_ref/doc/uid/TP40016142)
- [`DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/DemoBots/Introduction/Intro.html#//apple_ref/doc/uid/TP40015179)

## Topics

### Entities and Components
- [class GKEntity](gkentity.md)
  An object relevant to gameplay, with functionality entirely provided by a collection of component objects.
- [class GKComponent](gkcomponent.md)
  The abstract superclass for creating objects that add specific gameplay functionality to an entity.
- [class GKComponentSystem](gkcomponentsystem.md)
  Manages periodic update messages for all component objects of a specified class.
### State Machines
- [class GKState](gkstate.md)
  The abstract superclass for defining state-specific logic as part of a state machine.
- [class GKStateMachine](gkstatemachine.md)
  A finite-state machine—a collection of state objects that each define logic for a particular state of gameplay and rules for transitioning between states.
### Spatial Partitioning
- [class GKQuadtree](gkquadtree.md)
  A data structure for organizing objects based on their locations in a two-dimensional space.
- [class GKQuadtreeNode](gkquadtreenode.md)
  A helper class for managing the objects you organize in a quadtree.
- [class GKOctree](gkoctree.md)
  A data structure for organizing objects based on their locations in a three-dimensional space.
- [class GKOctreeNode](gkoctreenode.md)
  A helper class for managing the objects you organize in an octree.
- [class GKRTree](gkrtree.md)
  A data structure that adaptively organizes objects based on their locations in a two-dimensional space.
### Strategists
- [protocol GKStrategist](gkstrategist.md)
  A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.
- [class GKMinmaxStrategist](gkminmaxstrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [class GKMonteCarloStrategist](gkmontecarlostrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [protocol GKGameModel](gkgamemodel.md)
  Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.
- [protocol GKGameModelPlayer](gkgamemodelplayer.md)
  Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.
- [protocol GKGameModelUpdate](gkgamemodelupdate.md)
  Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.
### Decision Trees
- [class GKDecisionTree](gkdecisiontree.md)
  A data structure that models a set of specific questions, their possible answers, and the actions that follow from a series of answers.
- [class GKDecisionNode](gkdecisionnode.md)
  A node for use in manually creating decision trees, representing a specific question and possible answers, or an action that follows from answering other questions.
### Pathfinding
- [class GKGraph](gkgraph.md)
  A collection of nodes that describes the navigability of a game world and provides  methods to search for routes through that space.
- [class GKObstacleGraph](gkobstaclegraph.md)
  A navigation graph for 2D game worlds that creates a minimal network for precise pathfinding around obstacles.
- [class GKMeshGraph](gkmeshgraph.md)
  A navigation graph for 2D game worlds that creates a space-filling network for smooth pathfinding around obstacles.
- [class GKGridGraph](gkgridgraph.md)
  A navigation graph for 2D game worlds where movement is constrained to an integer grid.
- [class GKGraphNode](gkgraphnode.md)
  A single node in a navigation graph for use in pathfinding.
- [class GKGraphNode2D](gkgraphnode2d.md)
  A node in a navigation graph, associated with a point in continuous 2D space.
- [class GKGraphNode3D](gkgraphnode3d.md)
  A node in a navigation graph, associated with a point in continuous 3D space.
- [class GKGridGraphNode](gkgridgraphnode.md)
  A node in a navigation graph, associated with a position on a discrete two-dimensional grid.
### Agents, Goals, and Behaviors
- [class GKAgent](gkagent.md)
  A component that moves a game entity according to a set of goals and realistic constraints.
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
### Obstacles
- [class GKObstacle](gkobstacle.md)
  The abstract base class for objects representing impassable areas in a game world.
- [class GKCircleObstacle](gkcircleobstacle.md)
  A circular impassable area to be avoided by agents.
- [class GKSphereObstacle](gksphereobstacle.md)
  A spherical impassable volume to be avoided by agents.
- [class GKPolygonObstacle](gkpolygonobstacle.md)
  A polygon-shaped impassable area in a 2D game world.
### Procedural Noise
- [class GKNoiseSource](gknoisesource.md)
  The abstract superclass for procedural noise generators.
- [class GKNoise](gknoise.md)
  A representation of procedural noise, generated by a noise source, that you can use to process, transform, or combine noise.
- [class GKNoiseMap](gknoisemap.md)
  A sample of procedural noise data from which you can read noise values directly or create noise textures.
- [class GKCoherentNoiseSource](gkcoherentnoisesource.md)
  The abstract superclass for procedural noise generators that create coherent noise.
- [class GKBillowNoiseSource](gkbillownoisesource.md)
  A procedural noise generator whose output is a type of fractal coherent noise with smooth features.
- [class GKPerlinNoiseSource](gkperlinnoisesource.md)
  A procedural noise generator whose output is a type of fractal coherent noise resembling natural phenomena such as clouds and terrain.
- [class GKRidgedNoiseSource](gkridgednoisesource.md)
  A procedural noise generator whose output is a type of multifractal coherent noise with sharply defined features.
- [class GKVoronoiNoiseSource](gkvoronoinoisesource.md)
  A procedural noise generator whose output (also called Worley noise or cellular noise) divides space into discrete cells surrounding random seed points.
- [class GKCylindersNoiseSource](gkcylindersnoisesource.md)
  A procedural noise generator whose output is a 3D field of concentric cylindrical shells.
- [class GKSpheresNoiseSource](gkspheresnoisesource.md)
  A procedural noise generator whose output is a 3D field of concentric spherical shells.
- [class GKCheckerboardNoiseSource](gkcheckerboardnoisesource.md)
  A procedural noise generator whose output is an alternating square pattern.
- [class GKConstantNoiseSource](gkconstantnoisesource.md)
  A procedural noise generator that outputs a field of a single constant value.
### Randomization
- [protocol GKRandom](gkrandom.md)
  The common interface for all randomization classes in (or usable with) GameplayKit.
- [class GKRandomSource](gkrandomsource.md)
  The superclass for all basic randomization classes in GameplayKit.
- [class GKARC4RandomSource](gkarc4randomsource.md)
  A basic random number generator implementing the ARC4 algorithm, which is suitable for most gameplay mechanics.
- [class GKLinearCongruentialRandomSource](gklinearcongruentialrandomsource.md)
  A basic random number generator implementing the linear congruential generator algorithm, which is faster but less random than the default random source.
- [class GKMersenneTwisterRandomSource](gkmersennetwisterrandomsource.md)
  A basic random number generator implementing the Mersenne Twister algorithm, which is more random, but slower than the default random source.
- [class GKRandomDistribution](gkrandomdistribution.md)
  A generator for random numbers that fall within a specific range and that exhibit a specific distribution over multiple samplings.
- [class GKGaussianDistribution](gkgaussiandistribution.md)
  A generator for random numbers that follow a  (also known as a ) across multiple samplings.
- [class GKShuffledDistribution](gkshuffleddistribution.md)
  A generator for random numbers that are uniformly distributed across many samplings, but where short sequences of similar values are unlikely.
### Rule Systems
- [class GKRule](gkrule.md)
  A rule to be used in the context of a rule system, with a predicate to be tested and an action to be executed when the test succeeds.
- [class GKNSPredicateRule](gknspredicaterule.md)
  A rule for use in a rule system that uses a Foundation [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object to evaluate itself.
- [class GKRuleSystem](gkrulesystem.md)
  A list of rules, together with a context for evaluating them and interpreting results, for use in constructing data-driven logic or fuzzy logic systems.
### Xcode and SpriteKit Integration
- [class GKScene](gkscene.md)
  A container for associating GameplayKit objects with a SpriteKit scene.
- [protocol GKSceneRootNodeType](gkscenerootnodetype.md)
  Identifies scene classes from other frameworks that support embedded GameplayKit information.
- [class GKSKNodeComponent](gksknodecomponent.md)
  A component that manages a SpriteKit node.
### Reference
- [GameplayKit Constants](gameplaykit-constants.md)
- [GameplayKit Structures](gameplaykit-structures.md)
- [GameplayKit Enumerations](gameplaykit-enumerations.md)
### Classes
- [class GKSCNNodeComponent](gkscnnodecomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/GameplayKit)*