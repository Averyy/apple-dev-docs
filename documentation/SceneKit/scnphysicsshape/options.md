# options

**Framework**: SceneKit  
**Kind**: property

The options dictionary that was used to create the shape.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var options: [SCNPhysicsShape.Option : Any]? { get }
```

#### Discussion

You provide this dictionary in the [`init(geometry:options:)`](scnphysicsshape/init(geometry:options:).md) or [`init(node:options:)`](scnphysicsshape/init(node:options:).md) method. Use this dictionary along with the [`sourceObject`](scnphysicsshape/sourceobject.md) property to recover the information that was used to create the shape.

If the shape was created with the [`init(shapes:transforms:)`](scnphysicsshape/init(shapes:transforms:).md) method, this property’s value is `nil`.

## See Also

- [var sourceObject: Any](scnphysicsshape/sourceobject.md)
  The object that was used to create the shape.
- [var transforms: [NSValue]?](scnphysicsshape/transforms.md)
  The array of transforms that was used to create a compound shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/options)*