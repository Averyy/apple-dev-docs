# PredicateExpressions.StringContainsRegex

**Framework**: Foundation  
**Kind**: struct

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
- [init(subject: Subject, regex: Regex)](predicateexpressions/stringcontainsregex/init(subject:regex:).md)
### Instance Properties
- [let regex: Regex](predicateexpressions/stringcontainsregex/regex.md)
- [let subject: Subject](predicateexpressions/stringcontainsregex/subject.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/stringcontainsregex)*