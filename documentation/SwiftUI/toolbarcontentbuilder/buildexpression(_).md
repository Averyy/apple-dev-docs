# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds an expression within the builder.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : CustomizableToolbarContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : ToolbarContent
```

## See Also

### Building conditional toolbar content
- [static buildIf(_:)](./buildif%28_%29.md)
- [static buildEither(first:)](./buildeither%28first%29.md)
- [static buildEither(second:)](./buildeither%28second%29.md)
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildexpression(_:))*