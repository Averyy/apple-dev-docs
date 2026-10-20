# AccessibilityRotorContentBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Result builder you use to generate rotor entry content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@resultBuilder
struct AccessibilityRotorContentBuilder
```

## Topics

### Building navigation content
- [static buildBlock(_:)](./accessibilityrotorcontentbuilder/buildblock%28_%29.md)
- [static func buildIf<Content>(Content?) -> some AccessibilityRotorContent](./accessibilityrotorcontentbuilder/buildif%28_%29.md)
- [static func buildExpression<Content>(Content) -> Content](./accessibilityrotorcontentbuilder/buildexpression%28_%29.md)
  Builds an expression within the builder.

## See Also

### Creating rotors
- [protocol AccessibilityRotorContent](./accessibilityrotorcontent.md)
  Content within an accessibility rotor.
- [struct AccessibilityRotorEntry](./accessibilityrotorentry.md)
  A struct representing an entry in an Accessibility Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder)*