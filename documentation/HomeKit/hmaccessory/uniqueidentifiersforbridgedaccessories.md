# uniqueIdentifiersForBridgedAccessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSUUID *> * uniqueIdentifiersForBridgedAccessories;
```

## Discussion

This value is `nil` for accessories that aren’t bridges. See the [`isBridged`](./isbridged.md) property for more information about working with bridges.

## See Also

### Managing bridged accessories
- [var isBridged: Bool](./isbridged.md)
  A Boolean that indicates whether the accessory is accessed through a bridge.
- [var identifiersForBridgedAccessories: [UUID]?](./identifiersforbridgedaccessories.md)
  An array of identifiers for accessories available through a bridge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/uniqueidentifiersforbridgedaccessories)*