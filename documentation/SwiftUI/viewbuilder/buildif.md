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

- [static buildEither(first:)](viewbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.
- [static buildEither(second:)](viewbuilder/buildeither(second:).md)
  Builds a partial result from a condition that’s false.
- [static buildLimitedAvailability(_:)](viewbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildif(_:))*