# sourceItem

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A description of the item stored at the source.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var sourceItem: NSFileProviderItem { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderItem sourceItem;
```

## See Also

### Accessing the Operation’s Data
- [var targetSide: NSFileProviderTestingOperationSide](./targetside.md)
  The target location for the new item.
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The domain’s version when the system discovered the item at the source location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingcreation/sourceitem)*