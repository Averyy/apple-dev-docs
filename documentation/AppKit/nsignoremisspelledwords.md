# NSIgnoreMisspelledWords

**Framework**: AppKit  
**Kind**: protocol

A protocol that enables the Ignore button in the Spelling panel to function properly.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSIgnoreMisspelledWords
```

#### Overview

The Ignore button allows the user to accept a word that the spelling checker believes is misspelled. In order for this action to update the “ignored words” list for the document being checked, the [`NSIgnoreMisspelledWords`](nsignoremisspelledwords.md) protocol must be implemented.

This protocol is necessary because a list of ignored words is useful only if it pertains to the entire document being checked, but the spelling checker (that is, an [`NSSpellChecker`](nsspellchecker.md) object) does not check the entire document for spelling at once. The spelling checker returns as soon as it finds a misspelled word. Thus, it checks only a subset of the document at any one time. The user usually wants to check the entire document, so usually several spelling checks are run in succession until no misspelled words are found. This protocol allows the list of ignored words to be maintained per document, even though the spelling checks are not run per document.

The [`NSIgnoreMisspelledWords`](nsignoremisspelledwords.md) protocol specifies a  method, [`ignoreSpelling(_:)`](nsignoremisspelledwords/ignorespelling(_:).md), which should be implemented like this:

```objc
- (void)ignoreSpelling:(id)sender {
    [[NSSpellChecker sharedSpellChecker] ignoreWord:[[sender selectedCell] stringValue]
                                        inSpellDocumentWithTag: myDocumentTag];
}
```

The second argument to the [`NSSpellChecker`](nsspellchecker.md) method [`ignoreWord(_:inSpellDocumentWithTag:)`](nsspellchecker/ignoreword(_:inspelldocumentwithtag:).md) is a tag that the spell checker can use to distinguish the documents being checked. When the spell checker can distinguish the various documents, it can append new ignored words to the appropriate list.

To make the ignored words feature useful, the application must store a document’s ignored words list with the document. See the [`NSSpellChecker`](nsspellchecker.md) class description for more information.

## Topics

### Ignoring spellings
- [func ignoreSpelling(Any?)](nsignoremisspelledwords/ignorespelling(_:).md)

## Relationships

### Conforming Types
- [NSText](nstext.md)
- [NSTextView](nstextview.md)

## See Also

- [class NSSpellChecker](nsspellchecker.md)
  An interface to the Cocoa spell-checking service.
- [protocol NSChangeSpelling](nschangespelling.md)
  A protocol that responder objects can implement to correct a misspelled word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsignoremisspelledwords)*