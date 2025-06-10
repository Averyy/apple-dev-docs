# SCNAnimatable

**Framework**: SceneKit  
**Kind**: protocol

The common interface for attaching animations to nodes, geometries, materials, and other SceneKit objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol SCNAnimatable : NSObjectProtocol
```

## Mentions

- [Animating SceneKit Content](animating-scenekit-content.md)

#### Overview

SceneKit uses the same architecture as the Core Animation framework, allowing you to animate property changes implicitly or explicitly. For implicit animation, use the [`SCNTransaction`](scntransaction.md) class to quickly create simple animations with very little code. For more complex animations, explicitly create [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) objects, and use the methods in the [`SCNAnimatable`](scnanimatable.md) protocol to attach them to the SceneKit objects you want to animate. You also use the methods in this protocol to control any animations already attached to a SceneKit object.

For example, making a node spin continuously for as long as it appears in the scene graph requires explicitly creating an animation that repeats. The following code creates such an animation and attaches it to a node:

```objc
CABasicAnimation *rotationAnimation = [CABasicAnimation animationWithKeyPath:@"rotation"];
// Animate one complete revolution around the node's Y axis.
rotationAnimation.toValue = [NSValue valueWithSCNVector4:SCNVector4Make(0, 1, 0, M_PI * 2)];
rotationAnimation.duration = 10.0; // One revolution in ten seconds.
rotationAnimation.repeatCount = FLT_MAX; // Repeat the animation forever.
[node addAnimation:rotationAnimation forKey:nil]; // Attach the animation to the node to start it.
```

## Topics

### Managing Animations
- [func addAnimation(any SCNAnimationProtocol, forKey: String?)](scnanimatable/addanimation(_:forkey:).md)
  Adds an animation object for the specified key.
- [func animation(forKey: String) -> CAAnimation?](scnanimatable/animation(forkey:).md)
  Returns the animation with the specified key.
- [var animationKeys: [String]](scnanimatable/animationkeys.md)
  An array containing the keys of all animations currently attached to the object.
- [func removeAllAnimations()](scnanimatable/removeallanimations.md)
  Removes all the animations currently attached to the object.
- [func removeAnimation(forKey: String)](scnanimatable/removeanimation(forkey:).md)
  Removes the animation attached to the object with the specified key.
- [func removeAnimation(forKey: String, fadeOutDuration: CGFloat)](scnanimatable/removeanimation(forkey:fadeoutduration:).md)
  Removes the animation attached to the object with the specified key, smoothly transitioning out of the animation’s effect.
### Pausing and Resuming Animations
- [func pauseAnimation(forKey: String)](scnanimatable/pauseanimation(forkey:).md)
  Pauses the animation attached to the object with the specified key.
- [func resumeAnimation(forKey: String)](scnanimatable/resumeanimation(forkey:).md)
  Resumes a previously paused animation attached to the object with the specified key.
- [func isAnimationPaused(forKey: String) -> Bool](scnanimatable/isanimationpaused(forkey:).md)
  Returns a Boolean value indicating whether the animation attached to the object with the specified key is paused.
### Instance Methods
- [func addAnimationPlayer(SCNAnimationPlayer, forKey: String?)](scnanimatable/addanimationplayer(_:forkey:).md)
- [func animationPlayer(forKey: String) -> SCNAnimationPlayer?](scnanimatable/animationplayer(forkey:).md)
- [func removeAllAnimations(withBlendOutDuration: CGFloat)](scnanimatable/removeallanimations(withblendoutduration:).md)
- [func removeAnimation(forKey: String, blendOutDuration: CGFloat)](scnanimatable/removeanimation(forkey:blendoutduration:).md)
- [func setAnimationSpeed(CGFloat, forKey: String)](scnanimatable/setanimationspeed(_:forkey:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SCNAccelerationConstraint](scnaccelerationconstraint.md)
- [SCNAnimationPlayer](scnanimationplayer.md)
- [SCNAvoidOccluderConstraint](scnavoidoccluderconstraint.md)
- [SCNBillboardConstraint](scnbillboardconstraint.md)
- [SCNBox](scnbox.md)
- [SCNCamera](scncamera.md)
- [SCNCapsule](scncapsule.md)
- [SCNCone](scncone.md)
- [SCNConstraint](scnconstraint.md)
- [SCNCylinder](scncylinder.md)
- [SCNDistanceConstraint](scndistanceconstraint.md)
- [SCNFloor](scnfloor.md)
- [SCNGeometry](scngeometry.md)
- [SCNIKConstraint](scnikconstraint.md)
- [SCNLight](scnlight.md)
- [SCNLookAtConstraint](scnlookatconstraint.md)
- [SCNMaterial](scnmaterial.md)
- [SCNMaterialProperty](scnmaterialproperty.md)
- [SCNMorpher](scnmorpher.md)
- [SCNNode](scnnode.md)
- [SCNParticleSystem](scnparticlesystem.md)
- [SCNPlane](scnplane.md)
- [SCNPyramid](scnpyramid.md)
- [SCNReferenceNode](scnreferencenode.md)
- [SCNReplicatorConstraint](scnreplicatorconstraint.md)
- [SCNShape](scnshape.md)
- [SCNSliderConstraint](scnsliderconstraint.md)
- [SCNSphere](scnsphere.md)
- [SCNTechnique](scntechnique.md)
- [SCNText](scntext.md)
- [SCNTorus](scntorus.md)
- [SCNTransformConstraint](scntransformconstraint.md)
- [SCNTube](scntube.md)

## See Also

- [class SCNAnimationEvent](scnanimationevent.md)
  A container for a closure, a block in Objective-C, to be executed at a specific time during playback of an animation.
- [class SCNAnimation](scnanimation-swift.class.md)
- [class SCNAnimationPlayer](scnanimationplayer.md)
- [class SCNTimingFunction](scntimingfunction.md)
- [protocol SCNAnimationProtocol](scnanimationprotocol.md)
- [class SCNAnimation](scnanimation-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimatable)*