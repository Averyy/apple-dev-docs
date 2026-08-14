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
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Escapable](../swift/escapable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/conditional)*