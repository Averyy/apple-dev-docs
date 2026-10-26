# asCollisionResolution

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Returns the operation if it resolves a collision by renaming the new item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```objc
- (id<NSFileProviderTestingCollisionResolution>) asCollisionResolution;
```

#### Discussion

If the operation doesn’t conform to the [`NSFileProviderTestingCollisionResolution`](../nsfileprovidertestingcollisionresolution.md) protocol, this method returns `nil`.

## See Also

### Access the Operation Type
- [var type: NSFileProviderTestingOperationType](./type.md)
  The operation’s type.
- [- asChildrenEnumeration](./aschildrenenumeration.md)
  Returns the operation if it enumerates contained items.
- [- asContentFetch](./ascontentfetch.md)
  Returns the operation if it fetches an item’s content.
- [- asCreation](./ascreation.md)
  Returns the operation if it propagates the creation of an item.
- [- asDeletion](./asdeletion.md)
  Returns the operation if it propagates the deletion of an item.
- [- asIngestion](./asingestion.md)
  Returns the operation if it alerts the system to changes.
- [- asLookup](./aslookup.md)
  Returns the operation if it looks up an item.
- [- asModification](./asmodification.md)
  Returns the operation if it propagates a change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingoperation/ascollisionresolution)*