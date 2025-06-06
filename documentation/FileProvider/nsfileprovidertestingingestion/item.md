# item

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

A description of the item that changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var item: NSFileProviderItem? { get }
```

#### Discussion

This property is `nil` for deletion events.

## See Also

- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovidertestingingestion/itemidentifier.md)
  The unique identifier for the item that changed.
- [var side: NSFileProviderTestingOperationSide](nsfileprovidertestingingestion/side.md)
  The location where the change occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingingestion/item)*