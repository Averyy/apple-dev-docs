# isVertical

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines the geometric orientation of the split view’s dividers.

**Availability**:
- macOS

## Declaration

```swift
var isVertical: Bool { get set }
```

```objc
@property (getter=isVertical) BOOL vertical;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which indicates horizontal dividers and views that stack one above the other (top-to-bottom) in the containing split view controller’s view.

To specify vertical dividers and a horizontal (side-by-side) arrangement of views within a split view controller, implement this property to return [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/isvertical)*