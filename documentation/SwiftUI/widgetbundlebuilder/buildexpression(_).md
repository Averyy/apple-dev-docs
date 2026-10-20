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
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> some Widget where Content : ControlWidget
```

## See Also

### Bundling widgets
- [static func buildBlock() -> some Widget](./buildblock%28%29.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](./buildblock%28_%29.md)
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)
  Builds an availability check within the builder
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](./buildoptional%28_%29.md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildexpression(_:))*