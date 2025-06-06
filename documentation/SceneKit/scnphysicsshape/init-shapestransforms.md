# init(shapes:transforms:)

**Framework**: SceneKit  
**Kind**: init

Creates a new physics shape by combining others.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(shapes: [SCNPhysicsShape], transforms: [NSValue]?)
```

#### Return Value

A new physics shape object.

#### Discussion

An individual physics shape is defined in its own local coordinate space. Therefore, to describe the positions and orientations of multiple shapes relative to one another, you must use coordinate transformations.

## Parameters

- `shapes`: An array of   objects.
- `transforms`: An array of   objects containing   values, each of which is a transform for the physics shape at the corresponding index in the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/init(shapes:transforms:))*