# contentOffset

**Framework**: SwiftUI  
**Kind**: property

The content offset of the scroll view.

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
var contentOffset: CGPoint { get set }
```

#### Discussion

This is the position of the scroll view within its overall content size. This value may extend before zero or beyond the content size when the content insets of the scroll view are non-zero or when rubber banding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollgeometry/contentoffset)*