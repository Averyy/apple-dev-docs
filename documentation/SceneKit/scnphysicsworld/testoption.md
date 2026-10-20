# SCNPhysicsWorld.TestOption

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Keys in options dictionaries that affect how SceneKit searches for bodies in a collision, ray, or sweep test.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
struct TestOption
```

```c
typedef NSString * SCNPhysicsTestOption;
```

#### Discussion

Pass a dictionary containing one or more of these keys (with values as described above) for the `options` parameter when calling one of these methods:

- [`contactTestBetween(_:_:options:)`](./contacttestbetween%28_,_,options%29.md)
- [`contactTest(with:options:)`](./contacttest%28with,options%29.md)
- [`rayTestWithSegment(from:to:options:)`](./raytestwithsegment%28from,to,options%29.md)
- [`convexSweepTest(with:from:to:options:)`](./convexsweeptest%28with,from,to,options%29.md)

## Topics

### Type Properties
- [static let backfaceCulling: SCNPhysicsWorld.TestOption](./testoption/backfaceculling.md)
  The key for choosing whether to ignore back-facing polygons in physics shapes when searching for contacts.
- [static let collisionBitMask: SCNPhysicsWorld.TestOption](./testoption/collisionbitmask.md)
  The key for selecting which categories of physics bodies that SceneKit should test for contacts.
- [static let searchMode: SCNPhysicsWorld.TestOption](./testoption/searchmode.md)
  The key for selecting the number and order of contacts to be tested.
- [SCNPhysicsWorld.TestSearchMode](./testsearchmode.md)
  Options affecting how SceneKit searches for bodies in a collision, ray, or sweep test, used with the [`searchMode`](./testoption/searchmode.md) key.
### Initializers
- [init(rawValue: String)](./testoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsworld/testoption)*