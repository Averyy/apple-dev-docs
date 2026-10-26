# setShortcutSuggestions(_:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Suggests shortcuts the user may want to add to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func setShortcutSuggestions(_ suggestions: [INShortcut])
```

```objc
- (void) setShortcutSuggestions:(NSArray<INShortcut *> *) suggestions;
```

## Mentions

- [Offering Actions in the Shortcuts App](../../SiriKit/offering-actions-in-the-shortcuts-app.md)

#### Discussion

To replace the list of shortcut suggestions, call setShortcutSuggestions(_:), passing in a new list of suggestions. To remove suggestions made by your app, call the same method, passing in an empty array. For more information, see [Offering Actions in the Shortcuts App](../../SiriKit/offering-actions-in-the-shortcuts-app.md).

> **Note**:  Changes to the list of shortcut suggestions don’t effect shortcuts that the user added to Siri.

## Parameters

- `suggestions`: A list of suggested shortcuts that the Settings app shows to the user in the *Siri & Search* section.

## See Also

### Setting Suggested Shortcuts
- [class INShortcutReference](../inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invoiceshortcutcenter/setshortcutsuggestions(_:))*