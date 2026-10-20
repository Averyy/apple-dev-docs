# WidgetBundleBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A custom attribute that constructs a widget bundle’s body.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
struct WidgetBundleBuilder
```

#### Overview

Use the `@WidgetBundleBuilder` attribute to group multiple widgets listed in the [`body`](./widgetbundle/body-swift.property.md) property of a widget bundle. For example, the following code defines a widget bundle that consists of two widgets.

```swift
@main
struct GameWidgets: WidgetBundle {
   @WidgetBundleBuilder
   var body: some Widget {
       GameStatusWidget()
       CharacterDetailWidget()
   }
}
```

## Topics

### Bundling widgets
- [static func buildBlock() -> some Widget](./widgetbundlebuilder/buildblock%28%29.md)
  Builds an empty Widget from a block containing no statements, `{ }`.
- [static buildBlock(_:)](./widgetbundlebuilder/buildblock%28_%29.md)
- [static buildExpression(_:)](./widgetbundlebuilder/buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](./widgetbundlebuilder/buildlimitedavailability%28_%29.md)
  Builds an availability check within the builder
- [static func buildOptional((any Widget & _LimitedAvailabilityWidgetMarker)?) -> some Widget](./widgetbundlebuilder/buildoptional%28_%29.md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

### Implementing a widget bundle
- [var body: Self.Body](./widgetbundle/body-swift.property.md)
  Declares the group of widgets that an app supports.
- [associatedtype Body : Widget](./widgetbundle/body-swift.associatedtype.md)
  The type of widget that represents the content of the bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder)*