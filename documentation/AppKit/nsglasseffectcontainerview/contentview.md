# contentView

**Framework**: AppKit  
**Kind**: property

The view that contains descendant views to merge together when in proximity to each other.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var contentView: NSView? { get set }
```

#### Discussion

The glass effect container view does the following:

1. Elevates the z-order of descendants of `contentView` to position them above the `contentView`.
2. Merges descendants together if the views are sufficiently similar and within the proximity specified in [`spacing`](nsglasseffectcontainerview/spacing.md).
3. Processes similar glass effect views as a batch to improve performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglasseffectcontainerview/contentview)*