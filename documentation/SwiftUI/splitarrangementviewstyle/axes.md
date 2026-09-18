# axes(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a split arrangement that supports the given axes.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func axes(_ axes: Axis.Set) -> SplitArrangementViewStyle
```

#### Discussion

For example, you could make a split arrangement which will only split its views into a vertical split layout using the `vertical` axis.

```swift
ArrangementView {
    PrimaryContent()
} secondary: {
    SecondaryContent()
}
.arrangementViewStyle(.split.axes(.vertical))
```

## Parameters

- `axes`: The supported axes the view can split to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/splitarrangementviewstyle/axes(_:))*