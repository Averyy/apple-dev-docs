# JointTransforms

**Framework**: RealityKit  
**Kind**: struct

A set of animatable transform values for joints that collectively represent a single skeletal pose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct JointTransforms
```

#### Overview

This structure provides a template that informs an animation on how to animate a character. The resulting movement bases on the  ([`fromValue`](fromtobyanimation/fromvalue-6msd.md)) ,  ([`toValue`](fromtobyanimation/tovalue-813jk.md)) , or  values ([`byValue`](fromtobyanimation/byvalue-3bp3q.md)) you supply for a [`FromToByAnimation`](fromtobyanimation.md). The animation determines which joints take on the movement through its [`jointNames`](fromtobyanimation/jointnames.md) property.

#### Animate an Entitys Skeleton

The following code moves the joints of a 3D asset by specifying the joint, `joint1`, beginning, and ending values.

```swift
// Define the joint's pose at the start of the animation.
let fromTransforms: [Transform] = [Transform(scale: SIMD3<Float>(1, 2, 3), rotation: simd_quatf(ix: 5.0, iy: 6.0, iz: 7.0, r: 8.0), translation: SIMD3<Float>(10, 20, 30))]
let fromPose = JointTransforms(fromTransforms)

// Define the joint's pose at the end of the animation.
let toTransforms: [Transform] = [Transform(scale: SIMD3<Float>(10, 20, 30), rotation:
simd_quatf(ix: 50.0, iy: 60.0, iz: 70.0, r: 80.0), translation:
SIMD3<Float>(100, 200, 300)) ]
let toPose = JointTransforms(toTransforms)

// Indicate that the animation applies to the joint named 'joint1'.
let jointNames = ["joint1"]

// Configure the animation specifics.
var fromToBy = FromToByAnimation<JointTransforms>()
fromToBy.name = "anim"
fromToBy.blendLayer = 100
fromToBy.duration = 10.0
fromToBy.fillMode = .forwards
fromToBy.jointNames = jointNames
fromToBy.fromValue = fromPose
fromToBy.toValue = toPose
fromToBy.bindTarget = .transform

// Generate a resource from the animation.
let animationResource = fromToBy.create()
```

To run the animation on an entity and animate the joints, call `playAnimation(_:transitionDuration:startsPaused:)`. Optionally, you can control the animation’s playback by storing the returned controller object.

```swift
// Play the animation on an entity.
let entity = AnchorEntity(...)
let controller = entity.playAnimation(animationResource)

// Optionally control playback using the returned controller.
controller.pause()
```

## Topics

### Creating joint transforms
- [init()](jointtransforms/init.md)
  Initializes a collection of animatable transforms for a single skeletal pose.
- [init<S>(S)](jointtransforms/init(_:).md)
  Initializes a collection of transforms of a specific type for a single skeletal pose.
- [init(arrayLiteral: Transform...)](jointtransforms/init(arrayliteral:).md)
  Initializes a collection of animatable transforms using the argument elements for a single skeletal pose.
### Identifying joint transforms
- [JointTransforms.ArrayLiteralElement](jointtransforms/arrayliteralelement.md)
  The type of the elements of an array literal.
- [JointTransforms.Element](jointtransforms/element.md)
  An individual joint transform in the collection.
- [JointTransforms.Index](jointtransforms/index.md)
  A position of an individual joint transform in the collection.
### Inspecting joint transform details
- [var startIndex: JointTransforms.Index](jointtransforms/startindex.md)
  An index to the first joint transform in the collection.
- [var endIndex: JointTransforms.Index](jointtransforms/endindex.md)
  An index to the last joint transform in the collection.
### Accessing joint transforms
- [subscript(JointTransforms.Index) -> Transform](jointtransforms/subscript(_:).md)
  Accesses a single joint transform in the collection at the given index.
- [func index(after: JointTransforms.Index) -> JointTransforms.Index](jointtransforms/index(after:).md)
  Returns the position in the sequence of the joint that follows the given position.
- [func index(before: JointTransforms.Index) -> JointTransforms.Index](jointtransforms/index(before:).md)
  Returns the position in the sequence of the joint that preceeds the given position.
### Comparing joint transforms
- [static func == (JointTransforms, JointTransforms) -> Bool](jointtransforms/==(_:_:).md)
  Returns a Boolean value that indicates whether two collections of joints are equal.

## Relationships

### Conforms To
- [AnimatableData](animatabledata.md)
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/jointtransforms)*