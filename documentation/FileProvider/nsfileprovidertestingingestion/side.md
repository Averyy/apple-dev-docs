# side

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The location where the change occurred.

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

## See Also

### Accessing the Operation’s Data
- [var itemIdentifier: NSFileProviderItemIdentifier](./itemidentifier.md)
  The unique identifier for the item that changed.
- [var item: NSFileProviderItem?](./item.md)
  A description of the item that changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingingestion/side)*