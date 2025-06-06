# RegexComponent Implementations

**Framework**: RegexBuilder

## Topics

### Initializers
- [init(CharacterClass, CharacterClass...)](characterclass/init(_:_:).md)
  Creates a character class that combines the given classes in a union.
### Instance Properties
- [var regex: Regex<Substring>](characterclass/regex.md)
  The regular expression represented by this component.
### Type Aliases
- [CharacterClass.RegexOutput](characterclass/regexoutput.md)
  The output type for this regular expression.
### Type Properties
- [static var any: CharacterClass](characterclass/any.md)
  A character class that matches any element.
- [static var anyGraphemeCluster: CharacterClass](characterclass/anygraphemecluster.md)
  A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [static var anyNonNewline: CharacterClass](characterclass/anynonnewline.md)
  A character class that matches any element that isn’t a newline.
- [static var digit: CharacterClass](characterclass/digit.md)
  A character class that matches any digit.
- [static var hexDigit: CharacterClass](characterclass/hexdigit.md)
  A character class that matches any hexadecimal digit.
- [static var horizontalWhitespace: CharacterClass](characterclass/horizontalwhitespace.md)
  A character class that matches any element that is classified as horizontal whitespace.
- [static var newlineSequence: CharacterClass](characterclass/newlinesequence.md)
  A character class that matches any newline sequence.
- [static var verticalWhitespace: CharacterClass](characterclass/verticalwhitespace.md)
  A character class that matches any element that is classified as vertical whitespace.
- [static var whitespace: CharacterClass](characterclass/whitespace.md)
  A character class that matches any element that is classified as whitespace.
- [static var word: CharacterClass](characterclass/word.md)
  A character class that matches any element that is a “word character”.
### Type Methods
- [static func anyOf<S>(S) -> CharacterClass](characterclass/anyof(_:)-1s0kt.md)
  Returns a character class that matches any character in the given string or sequence.
- [static func anyOf<S>(S) -> CharacterClass](characterclass/anyof(_:)-zvpp.md)
  Returns a character class that matches any Unicode scalar in the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/regexcomponent-implementations)*