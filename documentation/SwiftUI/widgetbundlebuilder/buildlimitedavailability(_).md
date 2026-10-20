# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds an availability check within the builder

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ widget: some ControlWidget) -> any Widget & _LimitedAvailabilityWidgetMarker
```

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ widget: some Widget) -> any Widget & _LimitedAvailabilityWidgetMarker
```

## See Also

### Bundling widgets
- [static func buildBlock() -> some Widget](./buildblock%28%29.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](./buildblock%28_%29.md)
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](./buildoptional%28_%29.md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildlimitedavailability(_:))*