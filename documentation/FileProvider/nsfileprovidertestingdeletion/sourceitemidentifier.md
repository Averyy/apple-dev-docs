# sourceItemIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The unique identifier for the source item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var sourceItemIdentifier: NSFileProviderItemIdentifier { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderItemIdentifier sourceItemIdentifier;
```

## See Also

### Accessing the Operation’s Data
- [var targetSide: NSFileProviderTestingOperationSide](./targetside.md)
  The target location for the delete operation.
- [var targetItemIdentifier: NSFileProviderItemIdentifier](./targetitemidentifier.md)
  The unique identifier for the target item.
- [var targetItemBaseVersion: NSFileProviderItemVersion](./targetitembaseversion.md)
  The version of the deleted item.
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The domain’s version when the source location deleted the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingdeletion/sourceitemidentifier)*