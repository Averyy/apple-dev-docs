# isKindOf(entity:)

**Framework**: Core Data  
**Kind**: method

Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isKindOf(entity: NSEntityDescription) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is a sub-entity of `entity`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `entity`: An entity.

## See Also

- [var subentitiesByName: [String : NSEntityDescription]](nsentitydescription/subentitiesbyname.md)
  A dictionary containing the receiver’s sub-entities.
- [var subentities: [NSEntityDescription]](nsentitydescription/subentities.md)
  An array containing the sub-entities of the receiver.
- [var superentity: NSEntityDescription?](nsentitydescription/superentity.md)
  The super-entity of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/iskindof(entity:))*