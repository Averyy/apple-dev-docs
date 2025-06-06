# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`) through unmodified.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildBlock<Content>(_ content: Content) -> some Widget where Content : Widget
```

## See Also

- [static func buildBlock() -> some Widget](widgetbundlebuilder/buildblock.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildExpression(_:)](widgetbundlebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](widgetbundlebuilder/buildlimitedavailability(_:).md)
  Builds an availability check within the builder
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](widgetbundlebuilder/buildoptional(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildblock(_:))*