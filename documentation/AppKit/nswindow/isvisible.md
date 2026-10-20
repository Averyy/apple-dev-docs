# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is visible onscreen (even when it’s obscured by other windows).

**Availability**:
- macOS

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (readonly, getter=isVisible) BOOL visible;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window is onscreen (even if it’s obscured by other windows); otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var visibleRect: NSRect](../nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
### Managing Window Visibility and Occlusion State
- [var occlusionState: NSWindow.OcclusionState](./occlusionstate-swift.property.md)
  The occlusion state of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isvisible)*