# findSelected(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Begins a search for the selected content in your browser text view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func findSelected(_ sender: Any?)
```

```objc
- (void) findSelected:(id) sender;
```

## Discussion

UIKit calls this method when someone selects Use Selection for Find from an editing menu. Present the UI for finding text in your view, and use the selected text for the search. To present the standard system UI for finding text, and support standard keyboard shortcuts, add a [`UIFindInteraction`](../../UIKit/uifindinteraction.md) to your browser text view.

## Parameters

- `sender`: The object calling this method.

## See Also

### Finding and replacing text
- [func promptForReplace(Any?)](./promptforreplace%28_%29.md)
  Shows potential replacements for the selected content.
- [func replace(Any?)](./replace%28_%29.md)
  Removes the selected text and inputs the chosen replacement text.
- [func addShortcut(Any?)](./addshortcut%28_%29.md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/findselected(_:))*