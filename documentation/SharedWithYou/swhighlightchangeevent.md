# SWHighlightChangeEvent

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

An object that represents change activity for a highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWHighlightChangeEvent
```

```objc
@interface SWHighlightChangeEvent : NSObject
```

## Mentions

- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)

## Topics

### Creating a change event
- [init(highlight: SWHighlight, trigger: SWHighlightChangeEventTrigger)](./swhighlightchangeevent/init%28highlight,trigger%29.md)
  Creates and initializes a change event.
### Accessing event attributes
- [var highlightURL: URL](./swhighlightchangeevent/highlighturl.md)
  The URL of the hightlight.
- [var changeEventTrigger: SWHighlightChangeEventTrigger](./swhighlightchangeevent/changeeventtrigger.md)
  The type of change event for the highlight.
- [enum SWHighlightChangeEventTrigger](./swhighlightchangeeventtrigger.md)
  The type of change event for the highlight
### Initializers
- [init?(coder: NSCoder)](./swhighlightchangeevent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [SWHighlightEvent](./swhighlightevent.md)

## See Also

### Highlight events
- [protocol SWHighlightEvent](./swhighlightevent.md)
  A protocol that defines an activity that the system posts in response to a user action for a highlight.
- [class SWHighlightMembershipEvent](./swhighlightmembershipevent.md)
  An object that represents membership activity for a highlight.
- [class SWHighlightMentionEvent](./swhighlightmentionevent.md)
  An object that represents mention activity for a highlight.
- [class SWHighlightPersistenceEvent](./swhighlightpersistenceevent.md)
  An object that represents persistence activity for a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightchangeevent)*