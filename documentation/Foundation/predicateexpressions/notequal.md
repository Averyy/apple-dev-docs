# PredicateExpressions.NotEqual

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
struct NotEqual<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Equatable, LHS.Output == RHS.Output
```

## Topics

### Initializers
- [init(lhs: LHS, rhs: RHS)](predicateexpressions/notequal/init(lhs:rhs:).md)
### Instance Properties
- [let lhs: LHS](predicateexpressions/notequal/lhs.md)
- [let rhs: RHS](predicateexpressions/notequal/rhs.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/notequal)*