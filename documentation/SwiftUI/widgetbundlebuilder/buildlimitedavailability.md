# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an availability check within the builder

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
static func buildLimitedAvailability(_ widget: some ControlWidget) -> any Widget & _LimitedAvailabilityWidgetMarker
```

## See Also

- [static func buildBlock() -> some Widget](widgetbundlebuilder/buildblock.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](widgetbundlebuilder/buildblock(_:).md)
  Builds a single Widget written as a child view (e..g, `{ MyWidget() }`) through unmodified.
- [static buildExpression(_:)](widgetbundlebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](widgetbundlebuilder/buildoptional(_:).md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability(_:))*