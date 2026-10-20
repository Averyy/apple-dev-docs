# init(_:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a dynamic instructions instance that selects between two conditions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ branch: ConditionalDynamicInstructions<TrueContent, FalseContent>.Branch)
```

## Parameters

- `branch`: The condition to evaluate.

## See Also

### Creating an instance
- [ConditionalDynamicInstructions.Branch](./branch.md)
  An enumeration that represents a condition to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/conditionaldynamicinstructions/init(_:))*