# TupleDynamicInstructions

**Framework**: Foundation Models  
**Kind**: struct

A dynamic instructions type that represents a tuple.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct TupleDynamicInstructions<each Content> where repeat each Content : DynamicInstructions
```

## Topics

### Creating an instance
- [init(repeat each Content)](tupledynamicinstructions/init(_:).md)
  Creates a dynamic instructions instance that represents a tuple.

## Relationships

### Conforms To
- [DynamicInstructions](dynamicinstructions.md)

## See Also

- [struct DynamicInstructionsBuilder](dynamicinstructionsbuilder.md)
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type..
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/tupledynamicinstructions)*