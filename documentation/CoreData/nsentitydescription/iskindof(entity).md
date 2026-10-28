# isKindOf(entity:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isKindOf(entity: NSEntityDescription) -> Bool
```

```objc
- (BOOL) isKindOfEntity:(NSEntityDescription *) entity;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver is a sub-entity of `entity`, otherwise [`false`](../../Swift/false.md).

## Parameters

- `entity`: An entity.

## See Also

### Managing inheritance
- [var subentitiesByName: [String : NSEntityDescription]](./subentitiesbyname.md)
  A dictionary containing the receiver’s sub-entities.
- [var subentities: [NSEntityDescription]](./subentities.md)
  An array containing the sub-entities of the receiver.
- [var superentity: NSEntityDescription?](./superentity.md)
  The super-entity of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/iskindof(entity:))*