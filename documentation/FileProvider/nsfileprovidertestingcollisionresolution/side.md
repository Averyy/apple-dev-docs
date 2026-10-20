# side

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The item’s location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var side: NSFileProviderTestingOperationSide { get }
```

```objc
@property (nonatomic, readonly) NSFileProviderTestingOperationSide side;
```

#### Discussion

Most operations are symmetrical. They can affect either items stored locally, or items in the File Provider extension’s remote storage.

## See Also

### Accessing the Operation’s Data
- [var renamedItem: NSFileProviderItem](./renameditem.md)
  A description of the renamed item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingcollisionresolution/side)*