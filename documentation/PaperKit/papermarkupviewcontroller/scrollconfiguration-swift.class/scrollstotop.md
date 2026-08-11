# scrollsToTop

**Framework**: PaperKit  
**Kind**: property

A Boolean value that controls whether the scroll-to-top gesture is enabled.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var scrollsToTop: Bool { get set }
```

#### Discussion

When a person taps the status bar, the scroll view closest to the status bar scrolls to the top, but only if its `scrollsToTop` property is `true`, its delegate does not return `false` from `scrollViewShouldScrollToTop:`, and it is not already at the top.

On iPhone, this gesture works only if one on-screen scroll view has `scrollsToTop == true`. If more than one exists, none scroll to the top.

Default is `true`.

## See Also

- [var isScrollEnabled: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/isscrollenabled.md)
  A Boolean value that determines whether scrolling is enabled.
- [var isDirectionalLockEnabled: Bool](papermarkupviewcontroller/scrollconfiguration-swift.class/isdirectionallockenabled.md)
  A Boolean value that determines whether scrolling is disabled in a particular direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/scrollstotop)*