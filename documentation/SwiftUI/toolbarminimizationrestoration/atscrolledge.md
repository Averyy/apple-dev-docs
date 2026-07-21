# atScrollEdge

**Framework**: SwiftUI  
**Kind**: property

The toolbar restores only when the scroll view’s content reaches the scroll edge.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static let atScrollEdge: ToolbarMinimizationRestoration
```

#### Discussion

Mid-scroll reversals do not restore the toolbar. Currently this is only honored alongside [`onScrollDown`](toolbarminimizationbehavior/onscrolldown.md) and only for [`navigationBar`](toolbarplacement/navigationbar.md).

## See Also

- [static let automatic: ToolbarMinimizationRestoration](toolbarminimizationrestoration/automatic.md)
  The system determines the restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration/atscrolledge)*