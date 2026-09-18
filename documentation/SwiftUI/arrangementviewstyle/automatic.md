# automatic

**Framework**: SwiftUI  
**Kind**: property

The default arrangement view style.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@export(implementation)
nonisolated static var automatic: AutomaticArrangementViewStyle { get }
```

#### Discussion

Using this style, the arrangement view resolves to a [`SplitArrangementViewStyle`](splitarrangementviewstyle.md).

## See Also

- [static var overlay: OverlayArrangementViewStyle](arrangementviewstyle/overlay.md)
  An arrangement view style that layers the primary view over the secondary view in z-order.
- [static var split: SplitArrangementViewStyle](arrangementviewstyle/split.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyle/automatic)*