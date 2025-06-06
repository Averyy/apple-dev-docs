# showReplacements(forText:)

**Framework**: BrowserEngineKit  
**Kind**: method

Displays inline text replacements for the current selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func showReplacements(forText text: String)
```

#### Overview

Call this method to present system UI for suggesting text replacements, for example, when your browser text view receives [`promptForReplace(_:)`](berespondereditactions/promptforreplace(_:).md).

## See Also

- [func addShortcut(forText: String, from: CGRect)](betextinteraction/addshortcut(fortext:from:).md)
  Presents UI for a person to add a text-replacement shortcut to the keyboard dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/showreplacements(fortext:))*