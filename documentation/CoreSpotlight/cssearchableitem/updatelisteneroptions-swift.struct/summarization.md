# summarization

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Type Property

An option to summarize the contents of your searchable item. Specify this option only for items that contain emails, messages, or audio transcripts.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
static var summarization: CSSearchableItem.UpdateListenerOptions { get }
```

```c
CSSearchableItemUpdateListenerOptionSummarization
```

## See Also

### Getting the listener options attributes
- [static var priority: CSSearchableItem.UpdateListenerOptions](./priority.md)
  An option to classify the priority of SMS message content. Specify this option only if your item contains messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/updatelisteneroptions-swift.struct/summarization)*