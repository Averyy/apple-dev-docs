# buildEither(first:)

**Framework**: SwiftUI  
**Kind**: method

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
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent> where TrueContent : CustomizableToolbarContent, FalseContent : CustomizableToolbarContent
```

## See Also

- [static buildIf(_:)](toolbarcontentbuilder/buildif(_:).md)
- [static buildEither(second:)](toolbarcontentbuilder/buildeither(second:).md)
- [static buildExpression(_:)](toolbarcontentbuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](toolbarcontentbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildeither(first:))*