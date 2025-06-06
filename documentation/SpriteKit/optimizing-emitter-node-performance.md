# Optimizing Emitter Node Performance

**Framework**: SpriteKit

Use proven methods to rapidly create and play back performant particle effects.

#### Overview

Particle emitters in SpriteKit are one of the most powerful tools for building visual effects. However, if used incorrectly, particle emitters can be a bottleneck in the design and implementation of your app. Consider the following tips:

- Use Xcode to create and test your particle effects, then load the archives in your game.
- Adjust emitter properties sparingly inside your game code. Typically, you do this to specify properties that cannot be specified in the Xcode inspector or to control properties inside your game logic.
- Try to keep the number of onscreen particles to a minimum by creating particle emitters with a low birth rate, and specifying a short lifetime for particles. For example, instead of creating hundreds or thousands of particles per second, reduce the birth rate and increase the size of the particles slightly. Often, you can create effects with fewer particles but the same net visual appearance.
- Use actions on particles only when there isn’t another solution. Executing actions on individual particles is potentially very expensive, especially if the particle emitter also has a high birth rate.
- Assign a target node whenever the particles should be independent of the emitter node after they are spawned. For example, particles should be independent if the emitter node moves or rotates in the scene.
- Consider removing a particle emitter from the scene when it is not visible onscreen. Add it just before it becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/optimizing-emitter-node-performance)*