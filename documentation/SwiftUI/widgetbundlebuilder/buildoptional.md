# buildOptional(_:)

**Framework**: SwiftUI  
**Kind**: method

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
static func buildOptional(_ widget: (any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget
```

#### Discussion

Conditional statements in a [`WidgetBundleBuilder`](widgetbundlebuilder.md) can contain an `if` statement but not an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

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

- [static func buildBlock() -> some Widget](widgetbundlebuilder/buildblock.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](widgetbundlebuilder/buildblock(_:).md)
  Builds a single Widget written as a child view (e..g, `{ MyWidget() }`) through unmodified.
- [static buildExpression(_:)](widgetbundlebuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](widgetbundlebuilder/buildlimitedavailability(_:).md)
  Builds an availability check within the builder


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildoptional(_:))*