# didBegin(_:)

**Framework**: SpriteKit  
**Kind**: method

Called when two bodies first contact each other.

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
optional func didBegin(_ contact: SKPhysicsContact)
```

#### Discussion

The two physics bodies described in the contact parameter are not passed in a guaranteed order. The following code shows how you might respond to the beginning of a contact event to execute code if either physics body is owned by a node with the name `ground`.

Listing 1. Responding to a contact event.

```swift
func didBegin(_ contact: SKPhysicsContact) {
    if contact.bodyA.node?.name == "ground" || contact.bodyB.node?.name == "ground" {
        // execute code to respond to object hitting ground
    }
}
```

## Parameters

- `contact`: An object that describes the contact.

## See Also

- [func didEnd(SKPhysicsContact)](skphysicscontactdelegate/didend(_:).md)
  Called when the contact ends between two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/didbegin(_:))*