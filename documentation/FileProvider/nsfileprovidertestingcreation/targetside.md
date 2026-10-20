# targetSide

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The target location for the new item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var targetSide: NSFileProviderTestingOperationSide { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderTestingOperationSide targetSide;
```

## See Also

### Accessing the Operation’s Data
- [var sourceItem: NSFileProviderItem](./sourceitem.md)
  A description of the item stored at the source.
- [var domainVersion: NSFileProviderDomainVersion?](./domainversion.md)
  The domain’s version when the system discovered the item at the source location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingcreation/targetside)*