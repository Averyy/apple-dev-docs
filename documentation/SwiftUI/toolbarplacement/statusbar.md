# statusBar

**Framework**: SwiftUI  
**Kind**: property

The system status bar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static var statusBar: ToolbarPlacement { get }
```

#### Discussion

Use with [`toolbarVisibility(_:for:)`](view/toolbarvisibility(_:for:).md) to hide the status bar, or with [`toolbarColorScheme(_:for:)`](view/toolbarcolorscheme(_:for:).md) to specify the preferred status bar style.

```swift
content
    .toolbarVisibility(
        hideStatusBar ? .hidden : .automatic,
        for: .statusBar)
    // use light status bar on a dark background
    .toolbarColorScheme(.dark, for: .statusBar)
```

Using this placement with other toolbar customization APIs has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarplacement/statusbar)*