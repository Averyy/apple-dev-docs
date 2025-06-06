# Expression(_:)

**Framework**: Foundation  
**Kind**: macro

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
@freestanding
(expression) macro Expression<each Input, Output>(_ body: (repeat each Input) -> Output) -> Expression<repeat each Input, Output>
```

## See Also

- [macro Predicate<each Input>((repeat each Input) -> Bool) -> Predicate<repeat each Input>](predicate(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/expression(_:))*