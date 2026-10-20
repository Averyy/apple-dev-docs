# addShortcut(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Adds a text-replacement shortcut to the edit dictionary.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func addShortcut(_ sender: Any?)
```

```objc
- (void) addShortcut:(id) sender;
```

#### Discussion

To present the standard system UI for adding text-replacement shortcuts, call [`addShortcut(forText:from:)`](../betextinteraction/addshortcut%28fortext,from%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Finding and replacing text
- [func findSelected(Any?)](./findselected%28_%29.md)
  Begins a search for the selected content in your browser text view.
- [func promptForReplace(Any?)](./promptforreplace%28_%29.md)
  Shows potential replacements for the selected content.
- [func replace(Any?)](./replace%28_%29.md)
  Removes the selected text and inputs the chosen replacement text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/addshortcut(_:))*