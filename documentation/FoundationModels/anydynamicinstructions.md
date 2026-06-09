# AnyDynamicInstructions

**Framework**: Foundation Models  
**Kind**: struct

A dynamic instructions type that’s type-erased.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
  An empty dynamic instructions type..
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.
- [struct AnyTool](anytool.md)
  A tool that the framework invokes in dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/anydynamicinstructions)*