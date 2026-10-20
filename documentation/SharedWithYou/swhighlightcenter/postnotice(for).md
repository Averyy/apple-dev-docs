# postNotice(for:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Posts a specified event to the highlight center for display.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func postNotice(for event: any SWHighlightEvent)
```

```objc
- (void) postNoticeForHighlightEvent:(id<SWHighlightEvent>) event;
```

## Parameters

- `event`: The [`SWHighlightEvent`](../swhighlightevent.md) to add.

## See Also

### Posting highlight events
- [func clearNotices(for: SWCollaborationHighlight)](./clearnotices%28for%29.md)
  Clears the notices for a specified collaboration highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/postnotice(for:))*