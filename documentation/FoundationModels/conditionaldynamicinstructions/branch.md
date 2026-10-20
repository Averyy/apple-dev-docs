# ConditionalDynamicInstructions.Branch

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents a condition to evaluate.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Branch
```

Available when `TrueContent` conforms to `DynamicInstructions` and `FalseContent` conforms to `DynamicInstructions`.

## Topics

### Branch cases
- [ConditionalDynamicInstructions.Branch.falseContent(_:)](./branch/falsecontent%28_%29.md)
  A branch that represents false.
- [ConditionalDynamicInstructions.Branch.trueContent(_:)](./branch/truecontent%28_%29.md)
  A branch that represents true.

## See Also

### Creating an instance
- [init(ConditionalDynamicInstructions<TrueContent, FalseContent>.Branch)](./init%28_%29.md)
  Creates a dynamic instructions instance that selects between two conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/conditionaldynamicinstructions/branch)*