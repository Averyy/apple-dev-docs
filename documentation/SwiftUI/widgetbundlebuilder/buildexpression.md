# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an expression within the builder.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget
```

## See Also

- [static func buildBlock() -> some Widget](widgetbundlebuilder/buildblock.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](widgetbundlebuilder/buildblock(_:).md)
  Builds a single Widget written as a child view (e..g, `{ MyWidget() }`) through unmodified.
- [static buildLimitedAvailability(_:)](widgetbundlebuilder/buildlimitedavailability(_:).md)
  Builds an availability check within the builder
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](widgetbundlebuilder/buildoptional(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildexpression(_:))*