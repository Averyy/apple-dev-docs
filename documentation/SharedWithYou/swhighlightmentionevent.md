# SWHighlightMentionEvent

**Framework**: Shared with You  
**Kind**: class

An object that represents mention activity for a highlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWHighlightMentionEvent
```

## Mentions

- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)

## Topics

### Creating a mention event
- [init(highlight: SWHighlight, mentionedPersonCloudKitShareHandle: String)](swhighlightmentionevent/init(highlight:mentionedpersoncloudkitsharehandle:).md)
  Creates and initializes a mention event.
- [init(highlight: SWHighlight, mentionedPersonIdentity: SWPerson.Identity)](swhighlightmentionevent/init(highlight:mentionedpersonidentity:).md)
  Creates and initializes a mention event.
### Accessing the event person
- [var mentionedPersonHandle: String](swhighlightmentionevent/mentionedpersonhandle.md)
  The handle of the person the sender mentions.
### Initializers
- [init?(coder: NSCoder)](swhighlightmentionevent/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [SWHighlightEvent](swhighlightevent.md)

## See Also

- [protocol SWHighlightEvent](swhighlightevent.md)
  A protocol that defines an activity that the system posts in response to a user action for a highlight.
- [class SWHighlightChangeEvent](swhighlightchangeevent.md)
  An object that represents change activity for a highlight.
- [class SWHighlightMembershipEvent](swhighlightmembershipevent.md)
  An object that represents membership activity for a highlight.
- [class SWHighlightPersistenceEvent](swhighlightpersistenceevent.md)
  An object that represents persistence activity for a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightmentionevent)*