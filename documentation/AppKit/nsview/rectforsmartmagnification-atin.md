# rectForSmartMagnification(at:in:)

**Framework**: AppKit  
**Kind**: method

Returns the appropriate rectangle to use when magnifying around the specified point.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func rectForSmartMagnification(at location: NSPoint, in visibleRect: NSRect) -> NSRect
```

#### Return Value

The rectangle to use for magnification, specified in the view’s coordinate system. To get the default magnification behavior, return [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect).

#### Discussion

AppKit calls this method when magnifying content in a scroll view. If you do not override this method, or if you return [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect), the scroll view magnifies the view’s content around the specified point. If you override this method and return a custom rectangle, the scroll view adjusts the magnification behavior to accommodate the rectangle you provide.

Use this method to provide AppKit with rectangles for your view’s custom content. If your view’s content can be divided into logical groups of content, use the provided `location` and `visibleRect` parameters to determine which group is being targeted and then return the rectangle that fully encloses that group. For example, a view with multiple columns of content could return the rectangle for the targeted column. The returned rectangle should always fully enclose the content, regardless of whether that rectangle is larger than the visible rectangle.

## Parameters

- `location`: The location in your view’s coordinate system around which magnification is centered.
- `visibleRect`: The visible portion of the view. Use this value to help determine the specific content group you want to target for magnification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/rectforsmartmagnification(at:in:))*