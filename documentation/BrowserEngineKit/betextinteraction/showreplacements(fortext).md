# showReplacements(forText:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Displays inline text replacements for the current selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func showReplacements(forText text: String)
```

```objc
- (void) showReplacementsForText:(NSString *) text;
```

#### Discussion

Call this method to present system UI for suggesting text replacements, for example, when your browser text view receives [`promptForReplace(_:)`](../berespondereditactions/promptforreplace%28_%29.md).

## See Also

### Text replacements
- [func addShortcut(forText: String, from: CGRect)](./addshortcut%28fortext,from%29.md)
  Presents UI for a person to add a text-replacement shortcut to the keyboard dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/showreplacements(fortext:))*