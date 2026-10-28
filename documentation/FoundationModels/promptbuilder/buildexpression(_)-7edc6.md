# buildExpression(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with an expression.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<P>(_ expression: P) -> P where P : PromptRepresentable
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression(_ expression: Prompt) -> Prompt
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/promptbuilder/buildexpression(_:)-7edc6)*