# AnyTool

**Framework**: Foundation Models  
**Kind**: struct

A tool that the framework invokes in dynamic instructions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AnyTool
```

## Topics

### Creating a tool
- [init(some Tool)](anytool/init(_:).md)
  Creates a tool that wraps the given tool.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Tool](tool.md)

## See Also

- [struct DynamicInstructionsBuilder](dynamicinstructionsbuilder.md)
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type..
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/anytool)*