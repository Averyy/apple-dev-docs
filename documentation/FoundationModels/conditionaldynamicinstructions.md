# ConditionalDynamicInstructions

**Framework**: Foundation Models  
**Kind**: struct

A dynamic instructions type that conditionally selects between two conditions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ConditionalDynamicInstructions<TrueContent, FalseContent> where TrueContent : DynamicInstructions, FalseContent : DynamicInstructions
```

## Topics

### Creating an instance
- [init(ConditionalDynamicInstructions<TrueContent, FalseContent>.Branch)](conditionaldynamicinstructions/init(_:).md)
  Creates a dynamic instructions instance that selects between two conditions.
- [ConditionalDynamicInstructions.Branch](conditionaldynamicinstructions/branch.md)
  An enumeration that represents a condition to evaluate.

## Relationships

### Conforms To
- [DynamicInstructions](dynamicinstructions.md)

## See Also

- [struct DynamicInstructionsBuilder](dynamicinstructionsbuilder.md)
  A result builder that combines tools and other content into dynamic instructions.
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type.
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/conditionaldynamicinstructions)*