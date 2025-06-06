# Core Animation

**Framework**: Core Animation  
**Kind**: module

Render, compose, and animate visual elements.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 11.0+

#### Overview

Core Animation provides high frame rates and smooth animations without burdening the CPU or slowing down your app. Core Animation does most of the work of drawing each frame of an animation for you. You’re responsible for configuring the animation parameters, such as the start and end points, and Core Animation does the rest. It accelerates the rendering by handing over most of the work to dedicated graphics hardware. For more details, see [`Core Animation Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

## Topics

### Layer Basics
- [class CALayer](calayer.md)
  An object that manages image-based content and allows you to perform animations on that content.
- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [class CAConstraint](caconstraint.md)
  A representation of a single layout constraint between two layers.
- [protocol CALayoutManager](calayoutmanager.md)
  Methods that allow an object to manage the layout of a layer and its sublayers.
- [class CAConstraintLayoutManager](caconstraintlayoutmanager.md)
  An object that provides a constraint-based layout manager.
- [protocol CAAction](caaction.md)
  An interface that allows instances to respond to actions triggered by a Core Animation layer change.
### Text, Shapes, and Gradients
- [class CATextLayer](catextlayer.md)
  A layer that provides simple text layout and rendering of plain or attributed strings.
- [class CAShapeLayer](cashapelayer.md)
  A layer that draws a cubic Bezier spline in its coordinate space.
- [class CAGradientLayer](cagradientlayer.md)
  A layer that draws a color gradient over its background color, filling the shape of the layer.
### Animation
- [class CAAnimation](caanimation.md)
  The abstract superclass for animations in Core Animation.
- [protocol CAAnimationDelegate](caanimationdelegate.md)
  Methods your app can implement to respond when animations start and stop.
- [class CAPropertyAnimation](capropertyanimation.md)
  An abstract subclass for creating animations that manipulate the value of layer properties.
- [class CABasicAnimation](cabasicanimation.md)
  An object that provides basic, single-keyframe animation capabilities for a layer property.
- [class CAKeyframeAnimation](cakeyframeanimation.md)
  An object that provides keyframe animation capabilities for a layer object.
- [class CASpringAnimation](caspringanimation.md)
  An animation that applies a spring-like force to a layer’s properties.
- [class CATransition](catransition.md)
  An object that provides an animated transition between a layer’s states.
- [class CAValueFunction](cavaluefunction.md)
  An object that provides a flexible method of defining animated transformations.
### Animation Groups
- [class CAAnimationGroup](caanimationgroup.md)
  An object that allows multiple animations to be grouped and run concurrently.
- [class CATransaction](catransaction.md)
  A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.
### Animation Timing
- [func CACurrentMediaTime() -> CFTimeInterval](cacurrentmediatime().md)
  Returns the current absolute time, in seconds.
- [class CAMediaTimingFunction](camediatimingfunction.md)
  A function that defines the pacing of an animation as a timing curve.
- [protocol CAMediaTiming](camediatiming.md)
  Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [class CADisplayLink](cadisplaylink.md)
  A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.
### Particle Systems
- [class CAEmitterLayer](caemitterlayer.md)
  A layer that emits, animates, and renders a particle system.
- [class CAEmitterCell](caemittercell.md)
  The definition of a particle emitted by a particle layer.
### Advanced Layer Options
- [class CAScrollLayer](cascrolllayer.md)
  A layer that displays scrollable content larger than its own bounds.
- [class CATiledLayer](catiledlayer.md)
  A layer that provides a way to asynchronously provide tiles of the layer’s content, potentially cached at multiple levels of detail.
- [class CATransformLayer](catransformlayer.md)
  Objects used to create true 3D layer hierarchies, rather than the flattened hierarchy rendering model used by other layer types.
- [class CAReplicatorLayer](careplicatorlayer.md)
  A layer that creates a specified number of sublayer copies with varying geometric, temporal, and color transformations.
### Metal and OpenGL
- [class CAMetalLayer](cametallayer.md)
  A Core Animation layer that Metal can render into, typically displayed onscreen.
- [protocol CAMetalDrawable](cametaldrawable.md)
  A Metal drawable associated with a Core Animation layer.
- [class CAEAGLLayer](caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAEDRMetadata](caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CAOpenGLLayer](caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.
- [class CARenderer](carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.
### ProMotion
- [Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro](optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro.md)
  Provide custom animated content for ProMotion displays.
### Remote Display of Layer Content
- [class CARemoteLayerClient](caremotelayerclient.md)
  A legacy class for cross-process rendering.
- [class CARemoteLayerServer](caremotelayerserver.md)
  A legacy class for cross-process rendering.
### Transforms
- [Transforms](transforms.md)
  Define transform matrices to apply affine transformations to layers in Core Animation.
### Quartz Composer
- [class QCCompositionLayer](../Quartz/QCCompositionLayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
### Reference
- [Core Animation Structures](core-animation-structures.md)
- [Core Animation Constants](core-animation-constants.md)
- [QuartzCore Functions](quartzcore-functions.md)
- [Core Animation Data Types](core-animation-data-types.md)

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuartzCore)*