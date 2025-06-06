# AnyRegexOutput

**Framework**: Swift  
**Kind**: struct

The type-erased, dynamic output of a regular expression match.

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
struct AnyRegexOutput
```

#### Overview

When you find a match using regular expression that has `AnyRegexOutput` as its output type, you can find information about matches by iterating

## Topics

### Initializers
- [init<Output>(Regex<Output>.Match)](anyregexoutput/init(_:).md)
  Creates a dynamic regular expression match output from an existing match.
### Instance Methods
- [func extractValues<Output>(as: Output.Type) -> Output?](anyregexoutput/extractvalues(as:).md)
  Returns strongly-typed match output by converting this type-erased output to the specified type, if possible.
### Subscripts
- [subscript(String) -> AnyRegexOutput.Element?](anyregexoutput/subscript(_:)-6qdcr.md)
  Accesses the capture with the specified name, if a capture with that name exists.
### Default Implementations
- [BidirectionalCollection Implementations](anyregexoutput/bidirectionalcollection-implementations.md)
- [Collection Implementations](anyregexoutput/collection-implementations.md)
- [RandomAccessCollection Implementations](anyregexoutput/randomaccesscollection-implementations.md)
- [Sequence Implementations](anyregexoutput/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sequence](sequence.md)

## See Also

- [struct Regex](regex.md)
  A regular expression.
- [struct RegexRepetitionBehavior](regexrepetitionbehavior.md)
  Specifies how much to attempt to match when using a quantifier.
- [struct RegexSemanticLevel](regexsemanticlevel.md)
  A semantic level to use during regex matching.
- [struct RegexWordBoundaryKind](regexwordboundarykind.md)
  A word boundary algorithm to use during regex matching.
- [protocol RegexComponent](regexcomponent.md)
  A type that represents a regular expression.
- [protocol CustomConsumingRegexComponent](customconsumingregexcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput)*