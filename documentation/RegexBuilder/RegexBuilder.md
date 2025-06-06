# RegexBuilder

**Framework**: RegexBuilder  
**Kind**: module

Use an expressive domain-specific language to build regular expressions, for operations like searching and replacing in text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

#### Overview

Regular expressions, also known as regexes, are a powerful tool for matching patterns in text. Swift supports several ways to create a regular expression, including from a string, as a literal, and using this DSL. For example:

```swift
let word = OneOrMore(.word)
let emailPattern = Regex {
    Capture {
        ZeroOrMore {
            word
            "."
        }
        word
    }
    "@"
    Capture {
        word
        OneOrMore {
            "."
            word
        }
    }
}

let text = "My email is my.name@example.com."
if let match = text.firstMatch(of: emailPattern) {
    let (wholeMatch, name, domain) = match.output
    // wholeMatch is "my.name@example.com"
    // name is "my.name"
    // domain is "example.com"
}
```

## Topics

### Components
- [struct CharacterClass](characterclass.md)
  A class of characters that match in a regex.
- [struct Anchor](anchor.md)
  A regex component that matches a specific condition at a particular position in an input string.
- [struct Lookahead](lookahead.md)
  A regex component that allows a match to continue only if its contents match at the given location.
- [struct NegativeLookahead](negativelookahead.md)
  A regex component that allows a match to continue only if its contents do not match at the given location.
- [struct ChoiceOf](choiceof.md)
  A regex component that chooses exactly one of its constituent regex components when matching.
### Quantifiers
- [struct One](one.md)
  A regex component that matches exactly one occurrence of its underlying component.
- [struct Optionally](optionally.md)
  A regex component that matches zero or one occurrences of its underlying component.
- [struct ZeroOrMore](zeroormore.md)
  A regex component that matches zero or more occurrences of its underlying component.
- [struct OneOrMore](oneormore.md)
  A regex component that matches one or more occurrences of its underlying component.
- [struct Repeat](repeat.md)
  A regex component that matches a selectable number of occurrences of its underlying component.
- [struct Local](local.md)
  A regex component that represents an atomic group.
### Captures
- [struct Capture](capture.md)
  A regex component that saves the matched substring, or a transformed result, for access in a regex match.
- [struct TryCapture](trycapture.md)
  A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.
- [struct Reference](reference.md)
  A reference to a captured portion of a regular expression.
### Builders
- [enum RegexComponentBuilder](regexcomponentbuilder.md)
  A custom parameter attribute that constructs regular expressions from closures.
- [struct AlternationBuilder](alternationbuilder.md)
  A custom parameter attribute that constructs regular expression alternations from closures.
### Operators
- [func ... (Character, Character) -> CharacterClass]('...(_:_:)-16g2a.md)
  Returns a character class that includes the characters in the given range.
- [func ... (UnicodeScalar, UnicodeScalar) -> CharacterClass]('...(_:_:)-629xh.md)
  Returns a character class that includes the Unicode scalars in the given range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RegexBuilder)*