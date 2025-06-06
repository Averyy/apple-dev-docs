# build_contains(_:_:)

**Framework**: Foundation  
**Kind**: method

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
static func build_contains<Subject, Regex>(_ subject: Subject, _ regex: Regex) -> PredicateExpressions.StringContainsRegex<Subject, Regex> where Subject : PredicateExpression, Regex : PredicateExpression, Subject.Output : BidirectionalCollection, Regex.Output : RegexComponent, Subject.Output.SubSequence == Substring
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ferb)*