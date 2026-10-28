# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds an expression within the builder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> some Widget where Content : ControlWidget
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : Widget
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildexpression(_:)-hpbd)*