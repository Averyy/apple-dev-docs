# Predicate(_:)

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@freestanding(expression)
macro Predicate<each Input>(_ body: (repeat each Input) -> Bool) -> Predicate<repeat each Input>
```

## See Also

### Macros
- [macro Expression<each Input, Output>((repeat each Input) -> Output) -> Expression<repeat each Input, Output>](./expression%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicate(_:))*