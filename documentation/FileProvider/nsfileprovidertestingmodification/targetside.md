# targetSide

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

The target location for the modification operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var targetSide: NSFileProviderTestingOperationSide { get }
```

## See Also

- [var sourceItem: NSFileProviderItem](nsfileprovidertestingmodification/sourceitem.md)
  A description of the source item.
- [var changedFields: NSFileProviderItemFields](nsfileprovidertestingmodification/changedfields.md)
  A list of the fields that changed.
- [var targetItemIdentifier: NSFileProviderItemIdentifier](nsfileprovidertestingmodification/targetitemidentifier.md)
  The unique identifier for the target item.
- [var targetItemBaseVersion: NSFileProviderItemVersion](nsfileprovidertestingmodification/targetitembaseversion.md)
  The version of the changed item.
- [var domainVersion: NSFileProviderDomainVersion?](nsfileprovidertestingmodification/domainversion.md)
  The domain’s version when the change occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingmodification/targetside)*