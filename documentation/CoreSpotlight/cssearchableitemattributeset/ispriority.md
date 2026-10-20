# isPriority

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the mail or messages content represents a prioritized item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var isPriority: NSNumber? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * isPriority;
```

## Mentions

- [Generating summary and priority data for indexed items](../generating-summary-and-priority-data-for-indexed-items.md)

#### Discussion

During indexing, Apple Intelligence sets this property to `1` for any SMS content that requires priority classification. Use this property to prioritize the associated item’s content.

## See Also

### Handling Apple Intelligence prioritization and summarization
- [var textContentSummary: String?](./textcontentsummary.md)
  A string that presents the Apple Intelligence summarization of the item.
- [var transcribedTextContent: String?](./transcribedtextcontent.md)
  A string that represents the text the system transcribed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/ispriority)*