# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

Builds a partial result from a condition that’s false.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2> where T1 : ChartContent, T2 : ChartContent
```

#### Discussion

This method provides support for `if` statements with an `else` clause and `switch` statements. It produces optional chart content that is visible when the condition evaluates to `false`.

## Parameters

- `second`: The content to use if the condition is `false`.

## See Also

- [static buildEither(first:)](viewbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.
- [static buildIf(_:)](viewbuilder/buildif(_:).md)
  Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [static buildLimitedAvailability(_:)](viewbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildeither(second:))*