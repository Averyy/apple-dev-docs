# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds an expression within the builder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : AccessibilityRotorContent
```

## See Also

### Building navigation content
- [static buildBlock(_:)](./buildblock%28_%29.md)
- [static func buildIf<Content>(Content?) -> some AccessibilityRotorContent](./buildif%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder/buildexpression(_:))*