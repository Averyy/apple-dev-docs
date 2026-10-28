# identifiersForBridgedAccessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of identifiers for accessories available through a bridge.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`uniqueIdentifiersForBridgedAccessories`](./uniqueidentifiersforbridgedaccessories.md) instead.

## Declaration

```swift
var identifiersForBridgedAccessories: [UUID]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSUUID *> * identifiersForBridgedAccessories;
```

## Discussion

This value is `nil` for accessories that are not bridges.

## See Also

### Managing bridged accessories
- [var isBridged: Bool](./isbridged.md)
  A Boolean that indicates whether the accessory is accessed through a bridge.
- [var uniqueIdentifiersForBridgedAccessories: [UUID]?](./uniqueidentifiersforbridgedaccessories.md)
  An array of unique identifiers, each of which represents an accessory vended by the bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/identifiersforbridgedaccessories)*