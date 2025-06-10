# TipViewStyleConfiguration

**Framework**: TipKit  
**Kind**: struct

The container type that holds a tip’s configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct TipViewStyleConfiguration
```

## Topics

### Instance Properties
- [var actions: [Tips.Action]](tipviewstyleconfiguration/actions.md)
- [var image: Image?](tipviewstyleconfiguration/image.md)
- [var message: Text?](tipviewstyleconfiguration/message.md)
- [let tip: any Tip](tipviewstyleconfiguration/tip.md)
- [var title: Text?](tipviewstyleconfiguration/title.md)

## See Also

- [nonisolated func tipViewStyle(_ style: some TipViewStyle) -> some View
](../SwiftUI/View/tipViewStyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [protocol TipViewStyle](tipviewstyle.md)
  A type that applies custom appearance to all tips within a view hierarchy.
- [struct MiniTipViewStyle](minitipviewstyle.md)
  The default style for a TipView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipviewstyleconfiguration)*