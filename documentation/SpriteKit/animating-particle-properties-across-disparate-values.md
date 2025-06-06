# Animating Particle Properties Across Disparate Values

**Framework**: SpriteKit

Supply keyframe sequences to do linear or nonlinear particle animations.

#### Overview

An [`SKKeyframeSequence`](skkeyframesequence.md) object enables you to specify multiple values for an emitter node’s properties over a specific time period. The property values you choose may be arbitrary, which results in your ability to graph those property changes linearly or nonlinearly over time.

When you use a sequence, the values are not randomized. Instead, the sequence specifies all of the values of the property. Each keyframe value includes a value object and a timestamp. The timestamps are specified in a range from `0` to `1.0`, where `0` represents the birth of the particle and `1.0` represents its death.

The properties for which [`SKEmitterNode`](skemitternode.md) offers a keyframe sequence are:

| Property | Specifies | Example use |
| --- | --- | --- |
| [`particleColorSequence`](skemitternode/particlecolorsequence.md) | A sequence of arbitrary colors a particle should reflect over its lifetime. | Embers from a fire might specify the color sequence (white, yellow, orange, and brown) to appear hot, and then cool. |
| [`particleColorBlendFactorSequence`](skemitternode/particlecolorblendfactorsequence.md) | A sequence of color blend factors a particle should apply over its lifetime. | Embers from a fire might specify the color blend factor sequence (0, 1, 0, 1, … etc.) to simulate flickering. |
| [`particleScaleSequence`](skemitternode/particlescalesequence.md) | A sequence of sizes of a particle over its lifetime. | Balloons might use the scale sequence (0.1, 1, 1, 1, 0.1) to simulate inflation, and flying for some time before deflating. |
| [`particleAlphaSequence`](skemitternode/particlealphasequence.md) | A sequence of levels of transparency a particle undergoes over its lifetime. | Fireflies might specify a disparate sequence of alpha values to simulate random lighting patterns as they travel. |

The following code demonstrates using [`particleScaleSequence`](skemitternode/particlescalesequence.md) to animate the scale of an emitter node’s particles over their lifetime. Initially, the particles’ scale is `0.2` and then increases to `0.7` one-quarter of the way through the sequence. Three-quarters of the way through the sequence, the scale reaches its minimum size, `0.1`. It remains at this size until it dies.

## See Also

- [var particleAction: SKAction?](skemitternode/particleaction.md)
  An action executed by new particles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/animating-particle-properties-across-disparate-values)*