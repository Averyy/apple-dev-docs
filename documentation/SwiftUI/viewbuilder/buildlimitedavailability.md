# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
static func buildLimitedAvailability(_ content: any Commands) -> some Commands
```

## See Also

- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](viewbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static buildIf(_:)](viewbuilder/buildif(_:).md)
  Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:))*