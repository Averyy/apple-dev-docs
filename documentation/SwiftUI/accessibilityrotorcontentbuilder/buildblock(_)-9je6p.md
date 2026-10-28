# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func buildBlock<each Content>(_ content: repeat each Content) -> some AccessibilityRotorContent where repeat each Content : AccessibilityRotorContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<Content>(_ content: Content) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityrotorcontentbuilder/buildblock(_:)-9je6p)*