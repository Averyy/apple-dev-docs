# PredicateExpressions.StringContainsRegex

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct StringContainsRegex<Subject, Regex> where Subject : PredicateExpression, Regex : PredicateExpression, Subject.Output : BidirectionalCollection, Regex.Output : RegexComponent, Subject.Output.SubSequence == Substring
```

## Topics

### Initializers
- [init(subject: Subject, regex: Regex)](./stringcontainsregex/init%28subject,regex%29.md)
### Instance Properties
- [let regex: Regex](./stringcontainsregex/regex.md)
- [let subject: Subject](./stringcontainsregex/subject.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [PredicateExpression](../predicateexpression.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [StandardPredicateExpression](../standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/stringcontainsregex)*