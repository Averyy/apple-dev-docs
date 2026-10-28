# buildBlock(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

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
static func buildBlock<each Content>(_ contents: repeat each Content) -> TupleDynamicInstructions<repeat each Content> where repeat each Content : DynamicInstructions
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<T>(_ content: T) -> T where T : DynamicInstructions
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsbuilder/buildblock(_:)-4ulvp)*