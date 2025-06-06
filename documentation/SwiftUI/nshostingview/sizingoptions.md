# sizingOptions

**Framework**: SwiftUI  
**Kind**: property

The options for how the hosting view creates and updates constraints based on the size of its SwiftUI content.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency var sizingOptions: NSHostingSizingOptions { get set }
```

#### Discussion

NSHostingView can create minimum, maximum, and ideal (content size) constraints that are derived from its SwiftUI view content. These constraints are only created when Auto Layout constraints are otherwise being used in the containing window.

If the NSHostingView is set as the `contentView` of an `NSWindow`, it will also update the window’s `contentMinSize` and `contentMaxSize` based on the minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`, `intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to control this behavior. For instance, setting a value of `.minSize` will only create the constraints necessary to maintain the minimum size of the SwiftUI content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingView` relative to its displayed content, such as the always being displayed in a fixed frame, setting this to a value with fewer options can improve performance as it reduces the amount of layout measurements that need to be performed. If an `NSHostingView` has a `frame` that is smaller or larger than that required to display its SwiftUI content, the content will be centered within that frame.

## See Also

- [var intrinsicContentSize: NSSize](nshostingview/intrinsiccontentsize.md)
- [func setFrameSize(NSSize)](nshostingview/setframesize(_:).md)
- [var firstBaselineOffsetFromTop: CGFloat](nshostingview/firstbaselineoffsetfromtop.md)
- [var lastBaselineOffsetFromBottom: CGFloat](nshostingview/lastbaselineoffsetfrombottom.md)
- [var firstTextLineCenter: CGFloat?](nshostingview/firsttextlinecenter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/sizingoptions)*