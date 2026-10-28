# copiesOnScroll

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the clip view copies rendered images while scrolling.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: Setting this property has no effect.  NSClipView will always minimize the area of the document view that is invalidated.  To force invalidation of the document view, use -[NSView setNeedsDisplayInRect:].

## Declaration

```swift
var copiesOnScroll: Bool { get set }
```

```objc
@property BOOL copiesOnScroll;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the clip view copies its existing rendered image while scrolling (only drawing exposed portions of its document view); when it is [`false`](../../Swift/false.md), the view forces its contents to be redrawn each time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/copiesonscroll)*