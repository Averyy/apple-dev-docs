# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Builds a single Widget written as a child view (e..g, `{ MyWidget() }`) through unmodified.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildBlock<Content>(_ content: Content) -> some Widget where Content : Widget
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<each C>(_ c: repeat each C) -> some Widget where repeat each C : Widget
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundlebuilder/buildblock(_:)-230z4)*