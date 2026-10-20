# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func buildIf<Content>(_ content: Content?) -> Content?
```

**Other overloads**:

```swift
@export(implementation)
static func buildIf<Content>(_ content: Content?) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent
```

## See Also

### Conditionally building content
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildif(_:))*