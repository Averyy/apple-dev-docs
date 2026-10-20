# item

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A description of the item that changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var item: NSFileProviderItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSFileProviderItem item;
```

#### Discussion

This property is `nil` for deletion events.

## See Also

### Accessing the Operation’s Data
- [var itemIdentifier: NSFileProviderItemIdentifier](./itemidentifier.md)
  The unique identifier for the item that changed.
- [var side: NSFileProviderTestingOperationSide](./side.md)
  The location where the change occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingingestion/item)*