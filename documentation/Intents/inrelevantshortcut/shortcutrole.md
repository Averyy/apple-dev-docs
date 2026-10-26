# shortcutRole

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The role of the relevant shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var shortcutRole: INRelevantShortcutRole { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) INRelevantShortcutRole shortcutRole;
```

*macOS*

```objc
@property (atomic) INRelevantShortcutRole shortcutRole;
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

#### Discussion

The role provides a hint to Siri so it can provide a better experience to the user when suggesting the shortcut. The default is [`INRelevantShortcutRole.action`](../inrelevantshortcutrole/action.md).

## See Also

### Accessing Relevant Shortcut Information
- [var shortcut: INShortcut](./shortcut.md)
  A reference to the shortcut used to create the relevant shortcut.
- [enum INRelevantShortcutRole](../inrelevantshortcutrole.md)
  Roles for a relevant shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut/shortcutrole)*