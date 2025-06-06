# SWHighlightPersistenceEvent

**Framework**: Shared With You  
**Kind**: class

An object that represents persistence activity for a highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWHighlightPersistenceEvent
```

## Mentions

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)

## Topics

### Creating a persistence event
- [init(highlight: SWHighlight, trigger: SWHighlightPersistenceEventTrigger)](swhighlightpersistenceevent/init(highlight:trigger:).md)
  Creates and initializes a persistence event.
### Accessing an event trigger
- [var persistenceEventTrigger: SWHighlightPersistenceEventTrigger](swhighlightpersistenceevent/persistenceeventtrigger.md)
  The persistence event trigger for the highlight.
- [enum SWHighlightPersistenceEventTrigger](swhighlightpersistenceeventtrigger.md)
  Signifies the type of persistence event trigger.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SWHighlightEvent](swhighlightevent.md)

## See Also

- [protocol SWHighlightEvent](swhighlightevent.md)
  A protocol that defines an activity that the system posts in response to a user action for a highlight.
- [class SWHighlightChangeEvent](swhighlightchangeevent.md)
  An object that represents change activity for a highlight.
- [class SWHighlightMembershipEvent](swhighlightmembershipevent.md)
  An object that represents membership activity for a highlight.
- [class SWHighlightMentionEvent](swhighlightmentionevent.md)
  An object that represents mention activity for a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightpersistenceevent)*