# shortcut

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A reference to the shortcut used to create the relevant shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var shortcut: INShortcut { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INShortcut * shortcut;
```

*macOS*

```objc
@property (atomic, copy, readonly) INShortcut * shortcut;
```

## See Also

### Accessing Relevant Shortcut Information
- [var shortcutRole: INRelevantShortcutRole](./shortcutrole.md)
  The role of the relevant shortcut.
- [enum INRelevantShortcutRole](../inrelevantshortcutrole.md)
  Roles for a relevant shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut/shortcut)*