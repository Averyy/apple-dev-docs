# isBridged

**Framework**: HomeKit  
**Kind**: property

A Boolean that indicates whether the accessory is accessed through a bridge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isBridged: Bool { get }
```

#### Discussion

A bridge is a special type of accessory that allows you to communicate with accessories that can’t communicate directly with HomeKit. For example, a bridge might be a hub for multiple lights that use a communication protocol other than HomeKit Accessory Protocol.

Bridged accessories have the [`isBridged`](hmaccessory/isbridged.md) property set to [`true`](https://developer.apple.com/documentation/swift/true) and depend on the bridge to communicate with HomeKit. All other accessories, including the bridge itself, have an [`isBridged`](hmaccessory/isbridged.md) property setting of [`false`](https://developer.apple.com/documentation/swift/false).

To add a bridge to a home, use the home’s [`addAndSetupAccessories(completionHandler:)`](hmhome/addandsetupaccessories(completionhandler:).md) method, as you would for any other accessory. The accessories behind the bridge are automatically added to the home as well. The home’s delegate doesn’t receive a [`home(_:didAdd:)`](hmhomedelegate/home(_:didadd:)-6jcl7.md) delegate message for the bridge, but does receive one for each accessory behind the bridge.

When you add a bridge to a room, the accessories behind the bridge are not automatically added to the room because the bridge and its accessories might be located in different rooms. Manage each accessory’s room independently.

If you remove a bridge from the home, all of its accessories are also removed. On the other hand, you can’t directly remove a bridged accessory from the home. You can only remove the bridge.

In all other respects, you treat the accessories behind a bridge in the same way as any other accessory in a home. They appear in the home’s [`accessories`](hmhome/accessories.md) array like non-bridged accessories, and respond to all the same commands.

## See Also

- [var uniqueIdentifiersForBridgedAccessories: [UUID]?](hmaccessory/uniqueidentifiersforbridgedaccessories.md)
  An array of unique identifiers, each of which represents an accessory vended by the bridge.
- [var identifiersForBridgedAccessories: [UUID]?](hmaccessory/identifiersforbridgedaccessories.md)
  An array of identifiers for accessories available through a bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/isbridged)*