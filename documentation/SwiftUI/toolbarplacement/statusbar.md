# statusBar

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The system status bar.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
static var statusBar: ToolbarPlacement { get }
```

#### Discussion

Use with [`toolbarVisibility(_:for:)`](../view/toolbarvisibility%28_,for%29.md) to hide the status bar, or with [`toolbarColorScheme(_:for:)`](../view/toolbarcolorscheme%28_,for%29.md) to specify the preferred status bar style.

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