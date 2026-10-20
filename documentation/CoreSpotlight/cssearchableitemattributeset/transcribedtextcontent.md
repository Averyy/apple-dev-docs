# transcribedTextContent

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A string that represents the text the system transcribed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var transcribedTextContent: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * transcribedTextContent;
```

## Mentions

- [Generating summary and priority data for indexed items](../generating-summary-and-priority-data-for-indexed-items.md)

## See Also

### Handling Apple Intelligence prioritization and summarization
- [var isPriority: NSNumber?](./ispriority.md)
  A Boolean value that indicates whether the mail or messages content represents a prioritized item.
- [var textContentSummary: String?](./textcontentsummary.md)
  A string that presents the Apple Intelligence summarization of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/transcribedtextcontent)*