# scrollTo(y:)

**Framework**: SwiftUI  
**Kind**: method

Scrolls the position of the scroll view to the y value you provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func scrollTo(y: CGFloat)
```

#### Discussion

The scroll view chooses the x value based on the content insets of the scroll view and will clamp this value to only scroll to the size of its actual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(y:))*