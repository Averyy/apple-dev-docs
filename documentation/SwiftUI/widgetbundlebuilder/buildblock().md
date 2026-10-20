# buildBlock()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds an empty Widget from a block containing no statements, `{ }`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildBlock() -> some Widget
```

## See Also

### Bundling widgets
- [static buildBlock(_:)](./buildblock%28_%29.md)
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)
  Builds an availability check within the builder
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](./buildoptional%28_%29.md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildblock())*