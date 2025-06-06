# Regex

**Framework**: Swift  
**Kind**: struct

A regular expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Regex<Output>
```

#### Overview

Regular expressions are a concise way of describing a pattern, which can help you match or extract portions of a string. You can create a `Regex` instance using regular expression syntax, either in a regex literal or a string.

```swift
// 'keyAndValue' is created using a regex literal
let keyAndValue = /(.+?): (.+)/
// 'simpleDigits' is created from a pattern in a string
let simpleDigits = try Regex("[0-9]+")
```

You can use a `Regex` to search for a pattern in a string or substring. Call `contains(_:)` to check for the presence of a pattern, or `firstMatch(of:)` or `matches(of:)` to find matches.

```swift
let setting = "color: 161 103 230"
if setting.contains(simpleDigits) {
    print("'\(setting)' contains some digits.")
}
// Prints "'color: 161 103 230' contains some digits."
```

When you find a match, the resulting [`Regex.Match`](regex/match.md) type includes an [`output`](regex/match/output.md) property that contains the matched substring along with any captures:

```swift
if let match = setting.firstMatch(of: keyAndValue) {
    print("Key: \(match.1)")
    print("Value: \(match.2)")
}
// Key: color
// Value: 161 103 230
```

When you import the `RegexBuilder` module, you can also create `Regex` instances using a clear and flexible declarative syntax. Using this style, you can combine, capture, and transform regexes, `RegexBuilder` types, and custom parsers.

> **Note**:  Prior to Swift 6, you might need to write `#/myregex/#` instead of `/myregex/` when you make a regular expression using a literal. For more information, see [`Regular Expression Literals`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/lexicalstructure/#Regular-Expression-Literals) in  .

 Prior to Swift 6, you might need to write `#/myregex/#` instead of `/myregex/` when you make a regular expression using a literal. For more information, see [`Regular Expression Literals`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/lexicalstructure/#Regular-Expression-Literals) in  .

## Topics

### Structures
- [struct Match](regex/match.md)
  The result of matching a regular expression against a string.
### Initializers
- [init(() -> some RegexComponent<Output>)](regex/init(_:)-4ef55.md)
  Creates a regular expression using a RegexBuilder closure.
- [init(String) throws](regex/init(_:)-52kg.md)
  Creates a regular expression from the given string, using a dynamic capture list.
- [init<OtherOutput>(Regex<OtherOutput>)](regex/init(_:)-92siq.md)
  Creates a regular expression with a dynamic capture list from the given regular expression.
- [init?(Regex<AnyRegexOutput>, as: Output.Type)](regex/init(_:as:)-2ucu7.md)
  Creates a regular expression with a strongly-typed capture list from the given regular expression.
- [init(String, as: Output.Type) throws](regex/init(_:as:)-5z5nu.md)
  Creates a regular expression from the given string, using the specified capture type.
- [init(verbatim: String)](regex/init(verbatim:).md)
  Creates a regular expression that matches the given string exactly, as though every metacharacter in it was escaped.
### Instance Properties
- [var regex: Regex<Output>](regex/regex.md)
  The regular expression represented by this component.
### Instance Methods
- [func anchorsMatchLineEndings(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/anchorsmatchlineendings(_:).md)
  Returns a regular expression where the start and end of input anchors (`^` and `$`) also match against the start and end of a line.
- [func asciiOnlyCharacterClasses(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/asciionlycharacterclasses(_:).md)
  Returns a regular expression that matches only ASCII characters when matching character classes.
- [func asciiOnlyDigits(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/asciionlydigits(_:).md)
  Returns a regular expression that matches only ASCII characters as digits.
- [func asciiOnlyWhitespace(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/asciionlywhitespace(_:).md)
  Returns a regular expression that matches only ASCII characters as space characters.
- [func asciiOnlyWordCharacters(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/asciionlywordcharacters(_:).md)
  Returns a regular expression that matches only ASCII characters as word characters.
- [func contains(captureNamed: String) -> Bool](regex/contains(capturenamed:).md)
  Returns a Boolean value indicating whether a named capture with the given name exists.
- [func dotMatchesNewlines(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/dotmatchesnewlines(_:).md)
  Returns a regular expression where the “any” metacharacter (`.`) also matches against the start and end of a line.
- [func firstMatch(in: Substring) throws -> Regex<Output>.Match?](regex/firstmatch(in:)-45hz7.md)
  Returns the first match for this regex found in the given substring.
- [func firstMatch(in: String) throws -> Regex<Output>.Match?](regex/firstmatch(in:)-6s8x0.md)
  Returns the first match for this regex found in the given string.
- [func ignoresCase(Bool) -> Regex<Regex<Output>.RegexOutput>](regex/ignorescase(_:).md)
  Returns a regular expression that ignores case when matching.
- [func matchingSemantics(RegexSemanticLevel) -> Regex<Regex<Output>.RegexOutput>](regex/matchingsemantics(_:).md)
  Returns a regular expression that matches with the specified semantic level.
- [func prefixMatch(in: Substring) throws -> Regex<Output>.Match?](regex/prefixmatch(in:)-1an24.md)
  Returns a match if this regex matches the given substring at its start.
- [func prefixMatch(in: String) throws -> Regex<Output>.Match?](regex/prefixmatch(in:)-5oh8i.md)
  Returns a match if this regex matches the given string at its start.
- [func repetitionBehavior(RegexRepetitionBehavior) -> Regex<Regex<Output>.RegexOutput>](regex/repetitionbehavior(_:).md)
  Returns a regular expression where quantifiers use the specified behavior by default.
- [func wholeMatch(in: Substring) throws -> Regex<Output>.Match?](regex/wholematch(in:)-8hr88.md)
  Returns a match if this regex matches the given substring in its entirety.
- [func wholeMatch(in: String) throws -> Regex<Output>.Match?](regex/wholematch(in:)-9do8t.md)
  Returns a match if this regex matches the given string in its entirety.
- [func wordBoundaryKind(RegexWordBoundaryKind) -> Regex<Regex<Output>.RegexOutput>](regex/wordboundarykind(_:).md)
  Returns a regular expression that uses the specified word boundary algorithm.
### Type Aliases
- [typealias RegexOutput](regex/regexoutput.md)
  The output type for this regular expression.

## Relationships

### Conforms To
- [RegexComponent](regexcomponent.md)

## See Also

- [struct RegexRepetitionBehavior](regexrepetitionbehavior.md)
  Specifies how much to attempt to match when using a quantifier.
- [struct RegexSemanticLevel](regexsemanticlevel.md)
  A semantic level to use during regex matching.
- [struct RegexWordBoundaryKind](regexwordboundarykind.md)
  A word boundary algorithm to use during regex matching.
- [struct AnyRegexOutput](anyregexoutput.md)
  The type-erased, dynamic output of a regular expression match.
- [protocol RegexComponent](regexcomponent.md)
  A type that represents a regular expression.
- [protocol CustomConsumingRegexComponent](customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex)*