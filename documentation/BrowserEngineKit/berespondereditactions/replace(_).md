# replace(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Removes the selected text and inputs the chosen replacement text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func replace(_ sender: Any?)
```

```objc
- (void) replace:(id) sender;
```

#### Discussion

To invoke the standard system behavior for replacing text, call [`textInput(_:deferReplaceTextActionToSystem:)`](../betextinputdelegate/textinput%28_,deferreplacetextactiontosystem%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Finding and replacing text
- [func findSelected(Any?)](./findselected%28_%29.md)
  Begins a search for the selected content in your browser text view.
- [func promptForReplace(Any?)](./promptforreplace%28_%29.md)
  Shows potential replacements for the selected content.
- [func addShortcut(Any?)](./addshortcut%28_%29.md)
  Adds a text-replacement shortcut to the edit dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/replace(_:))*