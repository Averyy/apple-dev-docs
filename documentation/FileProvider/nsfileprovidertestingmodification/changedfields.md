# changedFields

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A list of the fields that changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var changedFields: NSFileProviderItemFields { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderItemFields changedFields;
```

## See Also

### Accessing the Operation’s Data
- [var sourceItem: NSFileProviderItem](./sourceitem.md)
  A description of the source item.
- [var targetSide: NSFileProviderTestingOperationSide](./targetside.md)
  The target location for the modification operation.
- [var targetItemIdentifier: NSFileProviderItemIdentifier](./targetitemidentifier.md)
  The unique identifier for the target item.
- [var targetItemBaseVersion: NSFileProviderItemVersion](./targetitembaseversion.md)
  The version of the changed item.
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The domain’s version when the change occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingmodification/changedfields)*