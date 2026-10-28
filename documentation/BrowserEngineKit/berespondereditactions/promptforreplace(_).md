# promptForReplace(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Shows potential replacements for the selected content.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func promptForReplace(_ sender: Any?)
```

```objc
- (void) promptForReplace:(id) sender;
```

## Discussion

To present the standard system UI for this action, call [`showReplacements(forText:)`](../betextinteraction/showreplacements%28fortext%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Finding and replacing text
- [func findSelected(Any?)](./findselected%28_%29.md)
  Begins a search for the selected content in your browser text view.
- [func replace(Any?)](./replace%28_%29.md)
  Removes the selected text and inputs the chosen replacement text.
- [func addShortcut(Any?)](./addshortcut%28_%29.md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/promptforreplace(_:))*