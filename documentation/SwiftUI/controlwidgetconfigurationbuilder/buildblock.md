# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

Passes a single control widget configuration written as a child control through unmodified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func buildBlock<Content>(_ content: Content) -> some ControlWidgetConfiguration where Content : ControlWidgetConfiguration
```

#### Discussion

An example of a single control widget configuration written as a child view is `{ StaticControlConfiguration(...) }`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgetconfigurationbuilder/buildblock(_:))*