# SCNPhysicsWorld.TestOption

**Framework**: SceneKit  
**Kind**: struct

Keys in options dictionaries that affect how SceneKit searches for bodies in a collision, ray, or sweep test.

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
struct TestOption
```

#### Discussion

Pass a dictionary containing one or more of these keys (with values as described above) for the `options` parameter when calling one of these methods:

- [`contactTestBetween(_:_:options:)`](scnphysicsworld/contacttestbetween(_:_:options:).md)
- [`contactTest(with:options:)`](scnphysicsworld/contacttest(with:options:).md)
- [`rayTestWithSegment(from:to:options:)`](scnphysicsworld/raytestwithsegment(from:to:options:).md)
- [`convexSweepTest(with:from:to:options:)`](scnphysicsworld/convexsweeptest(with:from:to:options:).md)

## Topics

### Type Properties
- [static let backfaceCulling: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](scnphysicsworld/testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.
- [SCNPhysicsWorld.TestSearchMode](scnphysicsworld/testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](scnphysicsworld/testoption/searchmode.md) key.
### Initializers
- [init(rawValue: String)](scnphysicsworld/testoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption)*