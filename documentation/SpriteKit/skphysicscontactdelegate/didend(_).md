# didEnd(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Called when the contact ends between two physics bodies.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
optional func didEnd(_ contact: SKPhysicsContact)
```

```objc
- (void) didEndContact:(SKPhysicsContact *) contact;
```

#### Discussion

The two physics bodies described in the contact parameter are not passed in a guaranteed order. The following code shows how you might respond to the end of a contact event to execute code if either physics body is owned by a node with the name `ground`.

Listing 1. Responding to a contact event

```swift
func didEnd(_ contact: SKPhysicsContact){
    if contact.bodyA.node?.name == "ground" || contact.bodyB.node?.name == "ground" {
        // execute code to respond to object hitting ground
    }
}
```

## Parameters

- `contact`: An object that describes the contact.

## See Also

### Responding to Contact Events
- [func didBegin(SKPhysicsContact)](./didbegin%28_%29.md)
  Called when two bodies first contact each other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/didend(_:))*