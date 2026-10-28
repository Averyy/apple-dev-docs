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
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : ToolbarContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Content>(_ content: Content) -> Content where Content : CustomizableToolbarContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildexpression(_:)-76w0r)*