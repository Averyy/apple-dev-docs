# accessibilityLargeContentViewerEnabled

**Framework**: SwiftUI  
**Kind**: property

Whether the Large Content Viewer is enabled.

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
var accessibilityLargeContentViewerEnabled: Bool { get }
```

#### Discussion

The system can automatically provide a large content view with [`accessibilityShowsLargeContentViewer()`](view/accessibilityshowslargecontentviewer().md) or you can provide your own with [`accessibilityShowsLargeContentViewer(_:)`](view/accessibilityshowslargecontentviewer(_:).md).

While it is not necessary to check this value before adding a large content view, it may be helpful if you need to adjust the behavior of a gesture. For example, a button with a long press handler might increase its long press duration so the user can read the text in the large content viewer first.

## See Also

- [func accessibilityShowsLargeContentViewer() -> some View](view/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](view/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilitylargecontentviewerenabled)*