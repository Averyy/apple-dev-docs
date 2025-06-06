# isPriority

**Framework**: Core Spotlight  
**Kind**: property

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

#### Discussion

When the value of this property is `1`, Apple Intelligence identified this email or message content as needing priority classification.

## See Also

- [var textContentSummary: String?](cssearchableitemattributeset/textcontentsummary.md)
  A string that presents the Apple Intelligence summarization of the item.
- [var transcribedTextContent: String?](cssearchableitemattributeset/transcribedtextcontent.md)
  A string that represents the text the system transcribed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/ispriority)*