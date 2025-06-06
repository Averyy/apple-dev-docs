# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method

Produces an optional view for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func buildIf<Content>(_ content: Content?) -> Content? where Content : View
```

## See Also

- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildLimitedAvailability<Content>(Content) -> AnyView](viewbuilder/buildlimitedavailability(_:).md)
  Processes view content for a conditional compiler-control statement that performs an availability check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildif(_:))*