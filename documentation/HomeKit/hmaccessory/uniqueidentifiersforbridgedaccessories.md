# uniqueIdentifiersForBridgedAccessories

**Framework**: HomeKit  
**Kind**: property

An array of unique identifiers, each of which represents an accessory vended by the bridge.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniqueIdentifiersForBridgedAccessories: [UUID]? { get }
```

#### Discussion

This value is `nil` for accessories that aren’t bridges. See the [`isBridged`](hmaccessory/isbridged.md) property for more information about working with bridges.

## See Also

- [var isBridged: Bool](hmaccessory/isbridged.md)
  A Boolean that indicates whether the accessory is accessed through a bridge.
- [var identifiersForBridgedAccessories: [UUID]?](hmaccessory/identifiersforbridgedaccessories.md)
  An array of identifiers for accessories available through a bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/uniqueidentifiersforbridgedaccessories)*