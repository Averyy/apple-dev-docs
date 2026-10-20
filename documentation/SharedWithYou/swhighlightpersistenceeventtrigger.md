# SWHighlightPersistenceEventTrigger

**Framework**: Shared with You  
**Kind**: enum  
**Role**: Enumeration

Signifies the type of persistence event trigger.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum SWHighlightPersistenceEventTrigger
```

```c
enum SWHighlightPersistenceEventTrigger : NSInteger;
```

## Topics

### Persistence actions
- [SWHighlightPersistenceEventTrigger.created](./swhighlightpersistenceeventtrigger/created.md)
  Signifies a creation event.
- [SWHighlightPersistenceEventTrigger.deleted](./swhighlightpersistenceeventtrigger/deleted.md)
  Signifies a deletion event.
- [SWHighlightPersistenceEventTrigger.renamed](./swhighlightpersistenceeventtrigger/renamed.md)
  Signifies a rename event.
- [SWHighlightPersistenceEventTrigger.moved](./swhighlightpersistenceeventtrigger/moved.md)
  Signifies a move event.
### Initializers
- [init?(rawValue: Int)](./swhighlightpersistenceeventtrigger/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing an event trigger
- [var persistenceEventTrigger: SWHighlightPersistenceEventTrigger](./swhighlightpersistenceevent/persistenceeventtrigger.md)
  The persistence event trigger for the highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightpersistenceeventtrigger)*