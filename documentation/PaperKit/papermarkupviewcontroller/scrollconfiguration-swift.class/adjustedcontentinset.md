# adjustedContentInset

**Framework**: PaperKit  
**Kind**: property

The insets that the system derives from the content insets and safe area insets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var adjustedContentInset: UIEdgeInsets { get }
```

#### Discussion

When `contentInsetAdjustmentBehavior` allows, the scroll view may incorporate its safe area insets into the adjusted content inset.

## See Also

- [var contentInset: NSEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-1ktjn.md)
  The custom distance to inset the content view from the scroll view edges.
- [var contentInset: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-3vn4v.md)
  The custom distance to inset the content view from the safe area or scroll view edges.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinsetadjustmentbehavior.md)
  The behavior for determining the adjusted content inset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/adjustedcontentinset)*