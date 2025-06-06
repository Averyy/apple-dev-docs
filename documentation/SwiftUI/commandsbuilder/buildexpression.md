# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an expression within the builder.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func buildExpression<Content>(_ content: Content) -> Content where Content : Commands
```

## See Also

- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](commandsbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](commandsbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildIf<C>(C?) -> C?](commandsbuilder/buildif(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static buildLimitedAvailability(_:)](commandsbuilder/buildlimitedavailability(_:).md)
  Processes commands for a conditional compiler-control statement that performs an availability check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandsbuilder/buildexpression(_:))*