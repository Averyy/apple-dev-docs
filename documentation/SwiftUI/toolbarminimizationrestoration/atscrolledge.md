# atScrollEdge

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The toolbar restores only when the scroll view’s content reaches the scroll edge.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
static let atScrollEdge: ToolbarMinimizationRestoration
```

## Discussion

Mid-scroll reversals do not restore the toolbar. Currently this is only honored alongside [`onScrollDown`](../toolbarminimizationbehavior/onscrolldown.md) and only for [`navigationBar`](../toolbarplacement/navigationbar.md).

## See Also

### Getting restoration options
- [static let automatic: ToolbarMinimizationRestoration](./automatic.md)
  The system determines the restoration behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarminimizationrestoration/atscrolledge)*