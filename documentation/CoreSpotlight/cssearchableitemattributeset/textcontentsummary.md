# textContentSummary

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A string that presents the Apple Intelligence summarization of the item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var textContentSummary: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * textContentSummary;
```

## Mentions

- [Generating summary and priority data for indexed items](../generating-summary-and-priority-data-for-indexed-items.md)

#### Discussion

For some types of content, Apple Intelligence generates a summary of the text content you provide and places it in this property. For information about how to generate summaries, see [Generating summary and priority data for indexed items](../generating-summary-and-priority-data-for-indexed-items.md).

## See Also

### Handling Apple Intelligence prioritization and summarization
- [var isPriority: NSNumber?](./ispriority.md)
  A Boolean value that indicates whether the mail or messages content represents a prioritized item.
- [var transcribedTextContent: String?](./transcribedtextcontent.md)
  A string that represents the text the system transcribed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/textcontentsummary)*