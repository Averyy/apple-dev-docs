# buildEither(first:)

**Framework**: SwiftUI  
**Kind**: method

Produces content for a conditional statement in a multi-statement closure when the condition is true.

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
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : View, FalseContent : View
```

## See Also

- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildIf<Content>(Content?) -> Content?](viewbuilder/buildif(_:).md)
  Produces an optional view for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static func buildLimitedAvailability<Content>(Content) -> AnyView](viewbuilder/buildlimitedavailability(_:).md)
  Processes view content for a conditional compiler-control statement that performs an availability check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildeither(first:))*