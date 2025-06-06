# Anchor

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that matches a specific condition at a particular position in an input string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct Anchor
```

#### Overview

You can use anchors to guarantee that a match only occurs at certain points in an input string, such as at the beginning of the string or at the end of a line.

## Topics

### Instance Properties
- [var inverted: Anchor](anchor/inverted.md)
  The inverse of this anchor, which matches at every position that this anchor does not.
### Type Properties
- [static var endOfLine: Anchor](anchor/endofline.md)
  An anchor that matches at the end of a line, including at the end of the input string.
- [static var endOfSubject: Anchor](anchor/endofsubject.md)
  An anchor that matches at the end of the input string.
- [static var endOfSubjectBeforeNewline: Anchor](anchor/endofsubjectbeforenewline.md)
  An anchor that matches at the end of the input string or at the end of the line immediately before the end of the string.
- [static var firstMatchingPositionInSubject: Anchor](anchor/firstmatchingpositioninsubject.md)
  An anchor that matches at the first position of a match in the input string.
- [static var startOfLine: Anchor](anchor/startofline.md)
  An anchor that matches at the start of a line, including the start of the input string.
- [static var startOfSubject: Anchor](anchor/startofsubject.md)
  An anchor that matches at the start of the input string.
- [static var textSegmentBoundary: Anchor](anchor/textsegmentboundary.md)
  An anchor that matches at a grapheme cluster boundary.
- [static var wordBoundary: Anchor](anchor/wordboundary.md)
  An anchor that matches at a word boundary.
### Default Implementations
- [RegexComponent Implementations](anchor/regexcomponent-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct CharacterClass](characterclass.md)
  A class of characters that match in a regex.
- [struct Lookahead](lookahead.md)
  A regex component that allows a match to continue only if its contents match at the given location.
- [struct NegativeLookahead](negativelookahead.md)
  A regex component that allows a match to continue only if its contents do not match at the given location.
- [struct ChoiceOf](choiceof.md)
  A regex component that chooses exactly one of its constituent regex components when matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/anchor)*