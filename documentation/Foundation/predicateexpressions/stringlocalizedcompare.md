# PredicateExpressions.StringLocalizedCompare

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
struct StringLocalizedCompare<Root, Other> where Root : PredicateExpression, Other : PredicateExpression, Root.Output : StringProtocol, Other.Output : StringProtocol
```

## Topics

### Initializers
- [init(root: Root, other: Other)](predicateexpressions/stringlocalizedcompare/init(root:other:).md)
### Instance Properties
- [let other: Other](predicateexpressions/stringlocalizedcompare/other.md)
- [let root: Root](predicateexpressions/stringlocalizedcompare/root.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/stringlocalizedcompare)*