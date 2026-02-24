# init(shapes:transforms:)

**Framework**: SceneKit  
**Kind**: init

Creates a new physics shape by combining others.

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
convenience init(shapes: [SCNPhysicsShape], transforms: [NSValue]?)
```

#### Return Value

A new physics shape object.

#### Discussion

An individual physics shape is defined in its own local coordinate space. Therefore, to describe the positions and orientations of multiple shapes relative to one another, you must use coordinate transformations.

## Parameters

- `shapes`: An array of [`SCNPhysicsShape`](scnphysicsshape.md) objects.
- `transforms`: An array of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects containing [`SCNMatrix4`](scnmatrix4-swift.struct.md) values, each of which is a transform for the physics shape at the corresponding index in the `shapes` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/init(shapes:transforms:))*