# RegexSemanticLevel

**Framework**: Swift  
**Kind**: struct

A semantic level to use during regex matching.

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
struct RegexSemanticLevel
```

#### Overview

The semantic level determines whether a regex matches with the same character-based semantics as string comparisons or by matching individual Unicode scalar values. See [`matchingSemantics(_:)`](regex/matchingsemantics(_:).md) for more about changing the semantic level for all or part of a regex.

## Topics

### Operators
- [static func == (RegexSemanticLevel, RegexSemanticLevel) -> Bool](regexsemanticlevel/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](regexsemanticlevel/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](regexsemanticlevel/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var graphemeCluster: RegexSemanticLevel](regexsemanticlevel/graphemecluster.md)
  Match at the character level.
- [static var unicodeScalar: RegexSemanticLevel](regexsemanticlevel/unicodescalar.md)
  Match at the Unicode scalar level.
### Default Implementations
- [Equatable Implementations](regexsemanticlevel/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [struct Regex](regex.md)
  A regular expression.
- [struct RegexRepetitionBehavior](regexrepetitionbehavior.md)
  Specifies how much to attempt to match when using a quantifier.
- [struct RegexWordBoundaryKind](regexwordboundarykind.md)
  A word boundary algorithm to use during regex matching.
- [struct AnyRegexOutput](anyregexoutput.md)
  The type-erased, dynamic output of a regular expression match.
- [protocol RegexComponent](regexcomponent.md)
  A type that represents a regular expression.
- [protocol CustomConsumingRegexComponent](customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexsemanticlevel)*