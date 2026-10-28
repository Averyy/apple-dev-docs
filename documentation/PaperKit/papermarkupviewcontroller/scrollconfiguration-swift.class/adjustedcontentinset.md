# adjustedContentInset

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The insets that the system derives from the content insets and safe area insets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
final var adjustedContentInset: UIEdgeInsets { get }
```

## Discussion

When `contentInsetAdjustmentBehavior` allows, the scroll view may incorporate its safe area insets into the adjusted content inset.

## See Also

### Configuring content insets
- [var contentInset: NSEdgeInsets](./contentinset-1ktjn.md)
  The custom distance to inset the content view from the scroll view edges.
- [var contentInset: UIEdgeInsets](./contentinset-3vn4v.md)
  The custom distance to inset the content view from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](./contentinsetadjustmentbehavior.md)
  The behavior for determining the adjusted content inset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/adjustedcontentinset)*