# addClip()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Uses the clipping path of the current graphics context to intersect the region that the path encloses, and makes the resulting shape the current clipping path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addClip()
```

```objc
- (void) addClip;
```

## Discussion

This method modifies the visible drawing area of the current graphics context. After calling it, subsequent drawing operations result in rendered content only if they occur within the fill area of the specified path.

> ❗ **Important**:  If you need to remove the clipping region to perform subsequent drawing operations, you must save the current graphics state (using the [`saveGState()`](../../CoreGraphics/cgcontext/savegstate%28%29.md) function) before calling this method. When you no longer need the clipping region, you can then restore the previous drawing properties and clipping region using the [`restoreGState()`](../../CoreGraphics/cgcontext/restoregstate%28%29.md) function.

The [`usesEvenOddFillRule`](./usesevenoddfillrule.md) property is used to determine whether the even-odd or non-zero rule is used to determine the area enclosed by the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/addclip())*