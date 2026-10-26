# INRelevantShortcutStore

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that saves relevant shortcuts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INRelevantShortcutStore
```

```objc
@interface INRelevantShortcutStore : NSObject
```

## Topics

### Getting the Shortcut Store
- [class var `default`: INRelevantShortcutStore](./inrelevantshortcutstore/default.md)
  The default relevant shortcut store.
### Setting Relevant Shortcuts
- [func setRelevantShortcuts([INRelevantShortcut], completionHandler: (((any Error)?) -> Void)?)](./inrelevantshortcutstore/setrelevantshortcuts%28_,completionhandler%29.md)
  Sets the relevant shortcuts.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Siri watch face
- [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [class INDefaultCardTemplate](./indefaultcardtemplate.md)
  A card template for customizing the Siri watch face for a shortcut.
- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [class INRelevantShortcut](./inrelevantshortcut.md)
  An object that defines a shortcut and its relevance to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcutstore)*