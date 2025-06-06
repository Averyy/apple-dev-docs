# PredicateExpressions.KeyPath

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
struct KeyPath<Root, Output> where Root : PredicateExpression
```

## Topics

### Initializers
- [init(root: Root, keyPath: any KeyPath<Root.Output, Output> & Sendable)](predicateexpressions/keypath/init(root:keypath:).md)
### Instance Properties
- [let keyPath: any KeyPath<Root.Output, Output> & Sendable](predicateexpressions/keypath/keypath.md)
- [var kind: PredicateExpressions.KeyPath<Root, Output>.CommonKeyPathKind?](predicateexpressions/keypath/kind.md)
- [let root: Root](predicateexpressions/keypath/root.md)
### Enumerations
- [PredicateExpressions.KeyPath.CommonKeyPathKind](predicateexpressions/keypath/commonkeypathkind.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [StandardPredicateExpression](standardpredicateexpression.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/keypath)*