# RegexWordBoundaryKind

**Framework**: Swift  
**Kind**: struct

A word boundary algorithm to use during regex matching.

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
struct RegexWordBoundaryKind
```

#### Overview

See [`wordBoundaryKind(_:)`](regex/wordboundarykind(_:).md) for information about specifying the word boundary kind for all or part of a regex.

## Topics

### Operators
- [static func == (RegexWordBoundaryKind, RegexWordBoundaryKind) -> Bool](regexwordboundarykind/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](regexwordboundarykind/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](regexwordboundarykind/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var `default`: RegexWordBoundaryKind](regexwordboundarykind/default.md)
  A word boundary algorithm that implements the “default word boundary” Unicode recommendation.
- [static var simple: RegexWordBoundaryKind](regexwordboundarykind/simple.md)
  A word boundary algorithm that implements the “simple word boundary” Unicode recommendation.
### Default Implementations
- [Equatable Implementations](regexwordboundarykind/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [struct Regex](regex.md)
  A regular expression.
- [struct RegexRepetitionBehavior](regexrepetitionbehavior.md)
  Specifies how much to attempt to match when using a quantifier.
- [struct RegexSemanticLevel](regexsemanticlevel.md)
  A semantic level to use during regex matching.
- [struct AnyRegexOutput](anyregexoutput.md)
  The type-erased, dynamic output of a regular expression match.
- [protocol RegexComponent](regexcomponent.md)
  A type that represents a regular expression.
- [protocol CustomConsumingRegexComponent](customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexwordboundarykind)*