# AnyDynamicInstructions

**Framework**: Foundation Models  
**Kind**: struct

A dynamic instructions type that’s type-erased.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AnyDynamicInstructions
```

## Topics

### Creating dynamic instructions
- [init(any DynamicInstructions)](anydynamicinstructions/init(_:).md)
  Creates an instance from the dynamic instructions you specify.
- [init(erasing: some DynamicInstructions)](anydynamicinstructions/init(erasing:).md)
  Creates an instance from the dynamic instructions you specify.

## Relationships

### Conforms To
- [DynamicInstructions](dynamicinstructions.md)

## See Also

- [struct DynamicInstructionsBuilder](dynamicinstructionsbuilder.md)
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type.
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/anydynamicinstructions)*