# CustomConsumingRegexComponent

**Framework**: Swift  
**Kind**: protocol

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
protocol CustomConsumingRegexComponent : RegexComponent
```

## Topics

### Instance Methods
- [func consuming(String, startingAt: String.Index, in: Range<String.Index>) throws -> (upperBound: String.Index, output: Self.RegexOutput)?](customconsumingregexcomponent/consuming(_:startingat:in:).md)
  Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

## Relationships

### Inherits From
- [RegexComponent](regexcomponent.md)

## See Also

- [struct Regex](regex.md)
  A regular expression.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/customconsumingregexcomponent)*