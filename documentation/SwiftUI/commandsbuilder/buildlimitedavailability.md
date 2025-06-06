# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method

Processes commands for a conditional compiler-control statement that performs an availability check.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 1.0+

## Declaration

```swift
static func buildLimitedAvailability(_ content: any Commands) -> some Commands
```

## See Also

- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](commandsbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](commandsbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildIf<C>(C?) -> C?](commandsbuilder/buildif(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static func buildExpression<Content>(Content) -> Content](commandsbuilder/buildexpression(_:).md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandsbuilder/buildlimitedavailability(_:))*