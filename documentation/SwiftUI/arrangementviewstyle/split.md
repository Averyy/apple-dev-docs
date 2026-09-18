# split

**Framework**: SwiftUI  
**Kind**: property

An arrangement view style that places the primary and secondary views side by side along one or more axes.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@export(implementation)
nonisolated static var split: SplitArrangementViewStyle { get }
```

#### Discussion

The split arrangement adapts its layout axis based on the available size and size class. Use this style for experiences that display two distinct pieces of content simultaneously, such as a music player alongside its lyrics or a calculator with a conversion panel.

Constrain which axes the split supports using [`axes(_:)`](splitarrangementviewstyle/axes(_:).md).

## See Also

- [static var automatic: AutomaticArrangementViewStyle](arrangementviewstyle/automatic.md)
  The default arrangement view style.
- [static var overlay: OverlayArrangementViewStyle](arrangementviewstyle/overlay.md)
  An arrangement view style that layers the primary view over the secondary view in z-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyle/split)*