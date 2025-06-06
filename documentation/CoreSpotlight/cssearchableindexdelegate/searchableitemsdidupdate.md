# searchableItemsDidUpdate(_:)

**Framework**: Core Spotlight  
**Kind**: method

Tells the delegate that the framework updated the list of searchable items.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
optional func searchableItemsDidUpdate(_ items: [CSSearchableItem])
```

#### Discussion

The framework calls this method when it updates an item with specific attributes; see [`CSSearchableItem.UpdateListenerOptions`](cssearchableitem/updatelisteneroptions-swift.struct.md) for Apple Intelligence attributes.

## Parameters

- `items`: The items the framework updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableitemsdidupdate(_:))*