# buildIf(_:)

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
static func buildIf<Content>(_ content: Content?) -> some AccessibilityRotorContent where Content : AccessibilityRotorContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildIf<Content>(_ content: Content?) -> Content?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildif(_:)-96k8e)*