# CharacterClass

**Framework**: RegexBuilder  
**Kind**: struct

A class of characters that match in a regex.

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
struct CharacterClass
```

#### Overview

A character class can represent individual characters, a group of characters, the set of character that match some set of criteria, or a set algebraic combination of all of the above.

## Topics

### Instance Properties
- [var inverted: CharacterClass](characterclass/inverted.md)
  A character class that matches any character that does not match this character class.
### Instance Methods
- [func intersection(CharacterClass) -> CharacterClass](characterclass/intersection(_:).md)
  Returns a character class from the intersection of this class and the given class.
- [func subtracting(CharacterClass) -> CharacterClass](characterclass/subtracting(_:).md)
  Returns a character class by subtracting the given class from this class.
- [func symmetricDifference(CharacterClass) -> CharacterClass](characterclass/symmetricdifference(_:).md)
  Returns a character class matching elements in one or the other, but not both, of this class and the given class.
- [func union(CharacterClass) -> CharacterClass](characterclass/union(_:).md)
  Returns a character class from the union of this class and the given class.
### Type Methods
- [static func generalCategory(Unicode.GeneralCategory) -> CharacterClass](characterclass/generalcategory(_:).md)
  Returns a character class that matches any element with the given Unicode general category.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct Anchor](anchor.md)
  A regex component that matches a specific condition at a particular position in an input string.
- [struct Lookahead](lookahead.md)
  A regex component that allows a match to continue only if its contents match at the given location.
- [struct NegativeLookahead](negativelookahead.md)
  A regex component that allows a match to continue only if its contents do not match at the given location.
- [struct ChoiceOf](choiceof.md)
  A regex component that chooses exactly one of its constituent regex components when matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass)*