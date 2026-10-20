# domainVersion

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The domain’s version when the change occurred.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var domainVersion: NSFileProviderDomainVersion? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSFileProviderDomainVersion * domainVersion;
```

## See Also

### Accessing the Operation’s Data
- [var sourceItem: NSFileProviderItem](./sourceitem.md)
  A description of the source item.
- [var changedFields: NSFileProviderItemFields](./changedfields.md)
  A list of the fields that changed.
- [var targetSide: NSFileProviderTestingOperationSide](./targetside.md)
  The target location for the modification operation.
- [var targetItemIdentifier: NSFileProviderItemIdentifier](./targetitemidentifier.md)
  The unique identifier for the target item.
- [var targetItemBaseVersion: NSFileProviderItemVersion](./targetitembaseversion.md)
  The version of the changed item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingmodification/domainversion)*