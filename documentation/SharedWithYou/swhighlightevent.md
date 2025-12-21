# SWHighlightEvent

**Framework**: Shared with You  
**Kind**: protocol

A protocol that defines an activity that the system posts in response to a user action for a highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol SWHighlightEvent : NSCopying, NSSecureCoding, NSObjectProtocol
```

## Mentions

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)

## Topics

### Accessing the URL
- [var highlightURL: URL](swhighlightevent/highlighturl.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
### Conforming Types
- [SWHighlightChangeEvent](swhighlightchangeevent.md)
- [SWHighlightMembershipEvent](swhighlightmembershipevent.md)
- [SWHighlightMentionEvent](swhighlightmentionevent.md)
- [SWHighlightPersistenceEvent](swhighlightpersistenceevent.md)

## See Also

- [class SWHighlightChangeEvent](swhighlightchangeevent.md)
  An object that represents change activity for a highlight.
- [class SWHighlightMembershipEvent](swhighlightmembershipevent.md)
  An object that represents membership activity for a highlight.
- [class SWHighlightMentionEvent](swhighlightmentionevent.md)
  An object that represents mention activity for a highlight.
- [class SWHighlightPersistenceEvent](swhighlightpersistenceevent.md)
  An object that represents persistence activity for a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightevent)*