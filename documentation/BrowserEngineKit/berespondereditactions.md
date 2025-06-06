# BEResponderEditActions

**Framework**: BrowserEngineKit  
**Kind**: protocol

A set of methods that defines extended interactions in browser text views.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BEResponderEditActions : UIResponderStandardEditActions
```

## Mentions

- [Supporting extended text interactions](support-extended-text-interactions.md)

#### Overview

Implement the methods in this protocol to support text interactions in your browser text view that conforms to [`BETextInput`](betextinput.md). To get the operating system’s standard behavior for an interaction, call [`BETextInteraction`](betextinteraction.md) methods in your implementation. For more information, see [`Supporting extended text interactions`](support-extended-text-interactions.md).

## Topics

### Finding and replacing text
- [func findSelected(Any?)](berespondereditactions/findselected(_:).md)
  Begins a search for the selected content in your browser text view.
- [func promptForReplace(Any?)](berespondereditactions/promptforreplace(_:).md)
  Shows potential replacements for the selected content.
- [func replace(Any?)](berespondereditactions/replace(_:).md)
  Removes the selected text and inputs the chosen replacement text.
- [func addShortcut(Any?)](berespondereditactions/addshortcut(_:).md)
  Adds a text-replacement shortcut to the edit dictionary.
### Defining and sharing text
- [func lookup(Any?)](berespondereditactions/lookup(_:).md)
  Presents a dictionary definition for the selected content.
- [func share(Any?)](berespondereditactions/share(_:).md)
  Presents UI for sharing the selected text.
### Translating and transliterating text
- [func translate(Any?)](berespondereditactions/translate(_:).md)
  Presents a translation of the selected text.
- [func transliterateChinese(Any?)](berespondereditactions/transliteratechinese(_:).md)
  Converts the selected text between traditional and simplified Chinese.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
### Inherited By
- [BETextInput](betextinput.md)

## See Also

- [class BETextInteraction](betextinteraction.md)
  An interaction you add to a text view to support extended text gestures.
- [protocol BETextInteractionDelegate](betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [enum BEGestureType](begesturetype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions)*