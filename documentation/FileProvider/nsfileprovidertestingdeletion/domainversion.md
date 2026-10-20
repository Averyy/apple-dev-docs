# domainVersion

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The domain’s version when the source location deleted the item.

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
- [var sourceItemIdentifier: NSFileProviderItemIdentifier](./sourceitemidentifier.md)
  The unique identifier for the source item.
- [var targetSide: NSFileProviderTestingOperationSide](./targetside.md)
  The target location for the delete operation.
- [var targetItemIdentifier: NSFileProviderItemIdentifier](./targetitemidentifier.md)
  The unique identifier for the target item.
- [var targetItemBaseVersion: NSFileProviderItemVersion](./targetitembaseversion.md)
  The version of the deleted item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingdeletion/domainversion)*