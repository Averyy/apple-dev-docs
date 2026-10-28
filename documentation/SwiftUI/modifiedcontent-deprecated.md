# Deprecated symbols

**Framework**: SwiftUI  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func accessibility(activationPoint:)](./modifiedcontent/accessibility%28activationpoint%29.md)
  Specifies the point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28addtraits%29.md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28hidden%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28hint%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28identifier%29.md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28inputlabels%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28label%29.md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28removetraits%29.md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28selectionidentifier%29.md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28sortpriority%29.md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Content, Modifier>](./modifiedcontent/accessibility%28value%29.md)
  Adds a textual description of the value that the view contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent-deprecated)*