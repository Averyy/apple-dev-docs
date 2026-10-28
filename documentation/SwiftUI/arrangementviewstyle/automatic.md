# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default arrangement view style.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
@export(implementation)
nonisolated static var automatic: AutomaticArrangementViewStyle { get }
```

Available when `Self` is `AutomaticArrangementViewStyle`.

## Overview

When you specify this style, the arrangement view uses [`SplitArrangementViewStyle`](../splitarrangementviewstyle.md).

## See Also

### Getting arrangement view styles
- [struct AutomaticArrangementViewStyle](../automaticarrangementviewstyle.md)
  The default arrangement view style.
- [static var overlay: OverlayArrangementViewStyle](./overlay.md)
  A style that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [struct OverlayArrangementViewStyle](../overlayarrangementviewstyle.md)
  A style that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [static var split: SplitArrangementViewStyle](./split.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.
- [struct SplitArrangementViewStyle](../splitarrangementviewstyle.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyle/automatic)*