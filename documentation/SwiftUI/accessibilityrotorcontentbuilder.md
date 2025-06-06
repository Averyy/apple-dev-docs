# AccessibilityRotorContentBuilder

**Framework**: SwiftUI  
**Kind**: struct

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
- [static func buildBlock<Content>(Content) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:).md)
- [static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:).md)
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildIf<Content>(Content?) -> some AccessibilityRotorContent](accessibilityrotorcontentbuilder/buildif(_:).md)
- [static func buildExpression<Content>(Content) -> Content](accessibilityrotorcontentbuilder/buildexpression(_:).md)
  Builds an expression within the builder.

## See Also

- [protocol AccessibilityRotorContent](accessibilityrotorcontent.md)
  Content within an accessibility rotor.
- [struct AccessibilityRotorEntry](accessibilityrotorentry.md)
  A struct representing an entry in an Accessibility Rotor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder)*