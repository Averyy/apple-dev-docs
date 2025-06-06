# identifiersForBridgedAccessories

**Framework**: HomeKit  
**Kind**: property

An array of identifiers for accessories available through a bridge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var identifiersForBridgedAccessories: [UUID]? { get }
```

#### Discussion

This value is `nil` for accessories that are not bridges.

## See Also

- [var isBridged: Bool](hmaccessory/isbridged.md)
  A Boolean that indicates whether the accessory is accessed through a bridge.
- [var uniqueIdentifiersForBridgedAccessories: [UUID]?](hmaccessory/uniqueidentifiersforbridgedaccessories.md)
  An array of unique identifiers, each of which represents an accessory vended by the bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/identifiersforbridgedaccessories)*