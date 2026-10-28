# splitView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The vertical split view to align with the toolbar separator.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var splitView: NSSplitView { get set }
```

```objc
@property (strong) NSSplitView * splitView;
```

## Discussion

The `splitView` must be in the same window as the toolbar containing the `NSTrackingSeparatorToolbarItem` before showing the toolbar.

## See Also

### configuring a tracking separator
- [var dividerIndex: Int](./dividerindex.md)
  The index of the split view divider to align with the tracking separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingseparatortoolbaritem/splitview)*