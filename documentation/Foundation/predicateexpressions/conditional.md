# PredicateExpressions.Conditional

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Conditional<Test, If, Else> where Test : PredicateExpression, If : PredicateExpression, Else : PredicateExpression, Test.Output == Bool, If.Output == Else.Output
```

## Topics

### Initializers
- [init(test: Test, trueBranch: If, falseBranch: Else)](predicateexpressions/conditional/init(test:truebranch:falsebranch:).md)
### Instance Properties
- [let falseBranch: Else](predicateexpressions/conditional/falsebranch.md)
- [let test: Test](predicateexpressions/conditional/test.md)
- [let trueBranch: If](predicateexpressions/conditional/truebranch.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/conditional)*