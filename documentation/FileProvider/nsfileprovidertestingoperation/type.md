# type

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The operation’s type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var type: NSFileProviderTestingOperationType { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderTestingOperationType type;
```

## See Also

### Access the Operation Type
- [- asChildrenEnumeration](./aschildrenenumeration.md)
  Returns the operation if it enumerates contained items.
- [- asCollisionResolution](./ascollisionresolution.md)
  Returns the operation if it resolves a collision by renaming the new item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingoperation/type)*