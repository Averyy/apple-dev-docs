# buildEither(first:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>
```

## See Also

### Conditionally building content
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static buildIf(_:)](./buildif%28_%29.md)
  Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildeither(first:))*