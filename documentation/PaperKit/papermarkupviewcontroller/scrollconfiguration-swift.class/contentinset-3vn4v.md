# contentInset

**Framework**: PaperKit  
**Kind**: property

The custom distance to inset the content view from the safe area or scroll view edges.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var contentInset: UIEdgeInsets { get set }
```

#### Discussion

Use this property to add additional scroll area around content. Default is `.zero`.

## See Also

- [var contentInset: NSEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-1ktjn.md)
  The custom distance to inset the content view from the scroll view edges.
- [var adjustedContentInset: UIEdgeInsets](papermarkupviewcontroller/scrollconfiguration-swift.class/adjustedcontentinset.md)
  The insets that the system derives from the content insets and safe area insets.
- [var contentInsetAdjustmentBehavior: UIScrollView.ContentInsetAdjustmentBehavior](papermarkupviewcontroller/scrollconfiguration-swift.class/contentinsetadjustmentbehavior.md)
  The behavior for determining the adjusted content inset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/contentinset-3vn4v)*