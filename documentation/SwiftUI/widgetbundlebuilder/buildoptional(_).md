# buildOptional(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

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
static func buildOptional(_ widget: (any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget
```

#### Discussion

Conditional statements in a [`WidgetBundleBuilder`](../widgetbundlebuilder.md) can contain an `if` statement but not an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some Widget {
    if #available(iOS 16, *) {
        WindowGroup {
            ContentView()
        }
    }
}
```

## See Also

### Bundling widgets
- [static func buildBlock() -> some Widget](./buildblock%28%29.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](./buildblock%28_%29.md)
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)
  Builds an availability check within the builder


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildoptional(_:))*