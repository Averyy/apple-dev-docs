# buildExpression(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with a dynamic instructions expression.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<T>(_ expression: T) -> T where T : DynamicInstructions
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression(_ tools: [any Tool]) -> some DynamicInstructions
```

```swift
static func buildExpression<T>(_ expression: T) -> some DynamicInstructions where T : Tool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder/buildexpression(_:)-2eawt)*