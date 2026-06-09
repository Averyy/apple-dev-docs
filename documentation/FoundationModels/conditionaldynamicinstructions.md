# ConditionalDynamicInstructions

**Framework**: Foundation Models  
**Kind**: struct

A dynamic instructions type that conditionally selects between two conditions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type..
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.
- [struct AnyTool](anytool.md)
  A tool that the framework invokes in dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/conditionaldynamicinstructions)*