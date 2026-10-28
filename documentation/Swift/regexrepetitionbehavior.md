# RegexRepetitionBehavior

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Specifies how much to attempt to match when using a quantifier.

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
struct RegexRepetitionBehavior
```

## Overview

See [`repetitionBehavior(_:)`](./regex/repetitionbehavior%28_%29.md) for more about specifying the default matching behavior for all or part of a regex.

## Topics

### Operators
- [static func == (RegexRepetitionBehavior, RegexRepetitionBehavior) -> Bool](./regexrepetitionbehavior/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](./regexrepetitionbehavior/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](./regexrepetitionbehavior/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var eager: RegexRepetitionBehavior](./regexrepetitionbehavior/eager.md)
  Match as much of the input string as possible, backtracking when necessary.
- [static var possessive: RegexRepetitionBehavior](./regexrepetitionbehavior/possessive.md)
  Match as much of the input string as possible, performing no backtracking.
- [static var reluctant: RegexRepetitionBehavior](./regexrepetitionbehavior/reluctant.md)
  Match as little of the input string as possible, expanding the matched region as necessary to complete a match.
### Default Implementations
- [Equatable Implementations](./regexrepetitionbehavior/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](./equatable.md)
- [Hashable](./hashable.md)

## See Also

### Regular Expressions
- [struct Regex](./regex.md)
  A regular expression.
- [struct RegexSemanticLevel](./regexsemanticlevel.md)
  A semantic level to use during regex matching.
- [struct RegexWordBoundaryKind](./regexwordboundarykind.md)
  A word boundary algorithm to use during regex matching.
- [struct AnyRegexOutput](./anyregexoutput.md)
  The type-erased, dynamic output of a regular expression match.
- [protocol RegexComponent](./regexcomponent.md)
  A type that represents a regular expression.
- [protocol CustomConsumingRegexComponent](./customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexrepetitionbehavior)*