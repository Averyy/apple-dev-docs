# collisionBitMask

**Framework**: SceneKit  
**Kind**: property

The key for selecting which categories of physics bodies that SceneKit should test for contacts.

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
static let collisionBitMask: SCNPhysicsWorld.TestOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an [`NSUInteger`](https://developer.apple.com/documentation/ObjectiveC/NSUInteger) value. SceneKit tests for contacts only with physics bodies whose [`categoryBitMask`](scnphysicsbody/categorybitmask.md) property overlaps with this bit mask. The default value is [`all`](scnphysicscollisioncategory/all.md), specifying that searches should test all physics bodies regardless of their category.

## See Also

- [static let backfaceCulling: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.
- [SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](scnphysicsworld/testoption/searchmode.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption/collisionbitmask)*