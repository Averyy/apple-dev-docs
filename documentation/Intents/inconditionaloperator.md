# INConditionalOperator

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating how search attributes are interpreted.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INConditionalOperator
```

```c
enum INConditionalOperator : NSInteger;
```

## Topics

### Constants
- [INConditionalOperator.all](./inconditionaloperator/all.md)
  All relevant attributes must be present for the search to yield a match. This is equivalent to an AND operator.
- [INConditionalOperator.any](./inconditionaloperator/any.md)
  One or more of the relevant attributes must be present for the search to yield a match. This is equivalent to an OR operator.
- [INConditionalOperator.none](./inconditionaloperator/none.md)
  None of the specified attributes must be present for the search to yield a match.
### Initializers
- [init?(rawValue: Int)](./inconditionaloperator/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inconditionaloperator)*