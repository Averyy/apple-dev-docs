# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a type-erased value that wraps the specified layout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<L>(_ layout: L) where L : Layout
```

#### Discussion

You can switch between type-erased layouts without losing the state of the subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anylayout/init(_:))*