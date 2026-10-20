# PredicateExpressions.KeyPath

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(root: Root, keyPath: any KeyPath<Root.Output, Output> & Sendable)](./keypath/init%28root,keypath%29.md)
### Instance Properties
- [let keyPath: any KeyPath<Root.Output, Output> & Sendable](./keypath/keypath.md)
- [var kind: PredicateExpressions.KeyPath<Root, Output>.CommonKeyPathKind?](./keypath/kind.md)
- [let root: Root](./keypath/root.md)
### Enumerations
- [PredicateExpressions.KeyPath.CommonKeyPathKind](./keypath/commonkeypathkind.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions/keypath)*