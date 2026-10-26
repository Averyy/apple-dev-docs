# INRelevantShortcutRole

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Roles for a relevant shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum INRelevantShortcutRole
```

```c
enum INRelevantShortcutRole : NSInteger;
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

## Topics

### Roles
- [INRelevantShortcutRole.action](./inrelevantshortcutrole/action.md)
  An action-based relevant shortcut.
- [INRelevantShortcutRole.information](./inrelevantshortcutrole/information.md)
  An informational-based relevant shortcut.
### Initializers
- [init?(rawValue: Int)](./inrelevantshortcutrole/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Relevant Shortcut Information
- [var shortcut: INShortcut](./inrelevantshortcut/shortcut.md)
  A reference to the shortcut used to create the relevant shortcut.
- [var shortcutRole: INRelevantShortcutRole](./inrelevantshortcut/shortcutrole.md)
  The role of the relevant shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcutrole)*