# contactDelegate

**Framework**: SpriteKit  
**Kind**: property

A delegate that is called when two physics bodies come in contact with each other.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
unowned(unsafe) var contactDelegate: (any SKPhysicsContactDelegate)? { get set }
```

#### Discussion

A contact is created when two physics bodies overlap and one of the physics bodies has a [`contactTestBitMask`](skphysicsbody/contacttestbitmask.md) property that overlaps with the other body’s [`categoryBitMask`](skphysicsbody/categorybitmask.md) property. By default, a physics body’s [`contactTestBitMask`](skphysicsbody/contacttestbitmask.md) is set to all bits cleared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsworld/contactdelegate)*