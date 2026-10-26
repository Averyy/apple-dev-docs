# INRelevantShortcut

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that defines a shortcut and its relevance to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INRelevantShortcut
```

```objc
@interface INRelevantShortcut : NSObject
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

## Topics

### Creating a Relevant Shortcut
- [init(shortcut: INShortcut)](./inrelevantshortcut/init%28shortcut%29.md)
  Creates a relevant shortcut with the specified shortcut.
### Accessing Relevant Shortcut Information
- [var shortcut: INShortcut](./inrelevantshortcut/shortcut.md)
  A reference to the shortcut used to create the relevant shortcut.
- [var shortcutRole: INRelevantShortcutRole](./inrelevantshortcut/shortcutrole.md)
  The role of the relevant shortcut.
- [enum INRelevantShortcutRole](./inrelevantshortcutrole.md)
  Roles for a relevant shortcut.
### Managing Relevance Providers
- [var relevanceProviders: [INRelevanceProvider]](./inrelevantshortcut/relevanceproviders.md)
  Additional relevance information attached to the shortcut.
### Managing the Siri Watch Face
- [var watchTemplate: INDefaultCardTemplate?](./inrelevantshortcut/watchtemplate.md)
  The template that the Siri watch face uses to display the relevant shortcut.
### Managing Widget Information
- [var widgetKind: String?](./inrelevantshortcut/widgetkind.md)
  An identifier that associates the shortcut with the widget it influences.
### Initializers
- [init?(coder: NSCoder)](./inrelevantshortcut/init%28coder%29.md)

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

## See Also

### Siri watch face
- [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [class INDefaultCardTemplate](./indefaultcardtemplate.md)
  A card template for customizing the Siri watch face for a shortcut.
- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [class INRelevantShortcutStore](./inrelevantshortcutstore.md)
  An object that saves relevant shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut)*