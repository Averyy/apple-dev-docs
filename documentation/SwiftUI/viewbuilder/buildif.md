# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method

Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.

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
static func buildIf<Content>(_ content: Content?) -> Content?
```

## See Also

- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static buildLimitedAvailability(_:)](viewbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildif(_:))*