# backfaceCulling

**Framework**: SceneKit  
**Kind**: property

The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.

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
static let backfaceCulling: SCNPhysicsWorld.TestOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`true`](https://developer.apple.com/documentation/Swift/true), specifying that the search should only return contacts with the exterior surfaces of any physics shapes. Change the value to [`false`](https://developer.apple.com/documentation/Swift/false) to consider contacts with both interior and exterior surfaces.

This key applies only to ray and convex sweep tests, and only to physics shapes created using the [`concavePolyhedron`](scnphysicsshape/shapetype/concavepolyhedron.md) option.

## See Also

- [static let collisionBitMask: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.
- [SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](scnphysicsworld/testoption/searchmode.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption/backfaceculling)*