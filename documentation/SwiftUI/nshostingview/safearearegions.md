# safeAreaRegions

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The safe area regions that this view controller adds to its view.

**Availability**:
- macOS 13.3+

## Declaration

```swift
@MainActor
@preconcurrency var safeAreaRegions: SafeAreaRegions { get set }
```

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the view layout behavior
- [class var requiresConstraintBasedLayout: Bool](./requiresconstraintbasedlayout.md)
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](./userinterfacelayoutdirection.md)
- [var isFlipped: Bool](./isflipped.md)
- [var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy](./layercontentsredrawpolicy.md)
- [func updateConstraints()](./updateconstraints%28%29.md)
- [func layout()](./layout%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/safearearegions)*