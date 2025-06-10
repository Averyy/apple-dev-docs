# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

Passes a single control widget template written as a child view through unmodified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func buildBlock<Content>(_ content: Content) -> some ControlWidgetTemplate where Content : ControlWidgetTemplate
```

#### Discussion

An example of a single control widget template written as a child view is `{ ControlWidgetToggle(...) }`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgettemplatebuilder/buildblock(_:))*