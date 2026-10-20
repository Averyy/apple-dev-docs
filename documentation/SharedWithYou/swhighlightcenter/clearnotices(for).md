# clearNotices(for:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Clears the notices for a specified collaboration highlight.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func clearNotices(for highlight: SWCollaborationHighlight)
```

```objc
- (void) clearNoticesForHighlight:(SWCollaborationHighlight *) highlight;
```

## Parameters

- `highlight`: The [`SWHighlightEvent`](../swhighlightevent.md) that contains the notices.

## See Also

### Posting highlight events
- [func postNotice(for: any SWHighlightEvent)](./postnotice%28for%29.md)
  Posts a specified event to the highlight center for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/clearnotices(for:))*