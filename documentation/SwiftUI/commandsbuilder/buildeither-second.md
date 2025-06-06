# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

Produces content for a conditional statement in a multi-statement closure when the condition is false.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where T : Commands, F : Commands
```

## See Also

- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](commandsbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildIf<C>(C?) -> C?](commandsbuilder/buildif(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static buildLimitedAvailability(_:)](commandsbuilder/buildlimitedavailability(_:).md)
  Processes commands for a conditional compiler-control statement that performs an availability check.
- [static func buildExpression<Content>(Content) -> Content](commandsbuilder/buildexpression(_:).md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandsbuilder/buildeither(second:))*