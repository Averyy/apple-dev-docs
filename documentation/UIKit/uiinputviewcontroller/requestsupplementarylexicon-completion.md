# requestSupplementaryLexicon(completion:)

**Framework**: UIKit  
**Kind**: method

Obtains a supplementary lexicon of term pairs in a custom keyboard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestSupplementaryLexicon() async -> UILexicon
```

#### Discussion

Call this method to obtain a [`UILexicon`](uilexicon.md) object containing a basic set of term pairs for use in autocorrection or textual suggestions based on user input. The [`UILexicon`](uilexicon.md) object contains words from various sources, including:

- Unpaired first names and last names from the user’s Address Book database
- Text shortcuts defined in the Settings > General > Keyboard > Shortcuts list
- A common words dictionary

Consider this lexicon as a supplement to a more complete lexicon of your own design.

## Parameters

- `completionHandler`: Code that you write to make use of the returned   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/requestsupplementarylexicon(completion:))*